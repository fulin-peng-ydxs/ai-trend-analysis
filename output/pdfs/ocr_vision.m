#import <Foundation/Foundation.h>
#import <Vision/Vision.h>
#import <ImageIO/ImageIO.h>
#import <CoreGraphics/CoreGraphics.h>

static int pageNumberFromPath(NSString *path, int fallback) {
    NSString *name = [[path lastPathComponent] stringByDeletingPathExtension];
    NSInteger idx = [name length] - 1;
    while (idx >= 0) {
        unichar c = [name characterAtIndex:idx];
        if (c < '0' || c > '9') {
            break;
        }
        idx--;
    }
    if (idx == (NSInteger)[name length] - 1) {
        return fallback;
    }
    NSString *digits = [name substringFromIndex:(NSUInteger)(idx + 1)];
    return [digits intValue];
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        if (argc < 3) {
            fprintf(stderr, "usage: ocr_vision output.json image1.png [image2.png ...]\n");
            return 2;
        }

        NSString *outputPath = [NSString stringWithUTF8String:argv[1]];
        NSMutableArray *items = [NSMutableArray array];

        for (int argIndex = 2; argIndex < argc; argIndex++) {
            NSString *path = [NSString stringWithUTF8String:argv[argIndex]];
            NSURL *url = [NSURL fileURLWithPath:path];
            CGImageSourceRef source = CGImageSourceCreateWithURL((__bridge CFURLRef)url, NULL);
            if (source == NULL) {
                fprintf(stderr, "failed to load image source: %s\n", argv[argIndex]);
                continue;
            }

            CGImageRef image = CGImageSourceCreateImageAtIndex(source, 0, NULL);
            if (image == NULL) {
                fprintf(stderr, "failed to load image: %s\n", argv[argIndex]);
                CFRelease(source);
                continue;
            }

            VNRecognizeTextRequest *request = [[VNRecognizeTextRequest alloc] init];
            request.recognitionLevel = VNRequestTextRecognitionLevelAccurate;
            request.usesLanguageCorrection = NO;
            request.recognitionLanguages = @[@"zh-Hans", @"en-US"];

            VNImageRequestHandler *handler = [[VNImageRequestHandler alloc] initWithCGImage:image options:@{}];
            NSError *ocrError = nil;
            if (![handler performRequests:@[request] error:&ocrError]) {
                fprintf(stderr, "ocr failed for %s: %s\n", argv[argIndex], [[ocrError description] UTF8String]);
                CGImageRelease(image);
                CFRelease(source);
                continue;
            }

            int page = pageNumberFromPath(path, argIndex - 1);
            for (VNRecognizedTextObservation *observation in request.results) {
                VNRecognizedText *candidate = [[observation topCandidates:1] firstObject];
                if (candidate == nil || candidate.string == nil) {
                    continue;
                }
                CGRect box = observation.boundingBox;
                [items addObject:@{
                    @"page": @(page),
                    @"text": candidate.string,
                    @"confidence": @(candidate.confidence),
                    @"x": @(box.origin.x),
                    @"y": @(box.origin.y),
                    @"width": @(box.size.width),
                    @"height": @(box.size.height)
                }];
            }

            CGImageRelease(image);
            CFRelease(source);
        }

        NSError *jsonError = nil;
        NSData *jsonData = [NSJSONSerialization dataWithJSONObject:items options:NSJSONWritingPrettyPrinted error:&jsonError];
        if (jsonData == nil) {
            fprintf(stderr, "failed to encode json: %s\n", [[jsonError description] UTF8String]);
            return 1;
        }
        if (![jsonData writeToFile:outputPath atomically:YES]) {
            fprintf(stderr, "failed to write output: %s\n", [outputPath UTF8String]);
            return 1;
        }
    }
    return 0;
}
