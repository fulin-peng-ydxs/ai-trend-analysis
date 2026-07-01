import Foundation
import Vision
import ImageIO

struct OCRItem: Codable {
    let page: Int
    let text: String
    let confidence: Float
    let x: Double
    let y: Double
    let width: Double
    let height: Double
}

func loadCGImage(_ path: String) -> CGImage? {
    let url = URL(fileURLWithPath: path)
    guard let source = CGImageSourceCreateWithURL(url as CFURL, nil) else {
        return nil
    }
    return CGImageSourceCreateImageAtIndex(source, 0, nil)
}

func pageNumber(from path: String, fallback: Int) -> Int {
    let name = URL(fileURLWithPath: path).deletingPathExtension().lastPathComponent
    if let match = name.range(of: #"\d+$"#, options: .regularExpression) {
        return Int(name[match]) ?? fallback
    }
    return fallback
}

let args = Array(CommandLine.arguments.dropFirst())
guard args.count >= 2 else {
    FileHandle.standardError.write(Data("usage: ocr_vision.swift output.json image1.png [image2.png ...]\n".utf8))
    exit(2)
}

let outputPath = args[0]
let imagePaths = Array(args.dropFirst())
var allItems: [OCRItem] = []

for (index, path) in imagePaths.enumerated() {
    guard let image = loadCGImage(path) else {
        FileHandle.standardError.write(Data("failed to load image: \(path)\n".utf8))
        continue
    }
    let page = pageNumber(from: path, fallback: index + 1)
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false
    request.recognitionLanguages = ["zh-Hans", "en-US"]
    if #available(macOS 13.0, *) {
        request.revision = VNRecognizeTextRequestRevision3
    }

    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    do {
        try handler.perform([request])
    } catch {
        FileHandle.standardError.write(Data("ocr failed for \(path): \(error)\n".utf8))
        continue
    }

    let observations = request.results ?? []
    for observation in observations {
        guard let candidate = observation.topCandidates(1).first else {
            continue
        }
        let box = observation.boundingBox
        allItems.append(
            OCRItem(
                page: page,
                text: candidate.string,
                confidence: candidate.confidence,
                x: Double(box.origin.x),
                y: Double(box.origin.y),
                width: Double(box.width),
                height: Double(box.height)
            )
        )
    }
}

let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
let data = try encoder.encode(allItems)
try data.write(to: URL(fileURLWithPath: outputPath))
