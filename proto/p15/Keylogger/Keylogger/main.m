//
//  main.m
//  Keylogger
//
//  Created by Andrew Head on 10/5/15.
//  Copyright © 2015 Andrew Head. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <Carbon/Carbon.h>
@import CoreGraphics;
@import CoreFoundation;


// Unknowns
// CFRunLoopRun

// I totally just guessed the below class definition would work out given this tutorial:
// http://www.tutorialspoint.com/objective_c/objective_c_classes_objects.htm
// It's too late to be thorough in the reading
@interface KeyPressData : NSObject {
    NSMutableArray *keyPresses;
    NSMutableArray *shiftPositions;
    NSArray *rules;
    bool shiftDown;
}
@property(nonatomic, readwrite) NSMutableArray *keyPresses;
@property(nonatomic, readwrite) NSMutableArray *shiftPositions;
@property(nonatomic, readwrite) NSArray *rules;
@property(nonatomic, readwrite) bool shiftDown;
@end

@implementation KeyPressData

@synthesize keyPresses;
@synthesize shiftPositions;
@synthesize rules;
@synthesize shiftDown;

-(id)init {
    self = [super init];
    shiftDown = false;
    return self;
}

@end

char upperCase(char c) {
    if (c >= 97 && c <= 122) {
        return toupper(c);
    } else if (c == ',') {
        return '<';
    } else if (c == '.') {
        return '>';
    } else if (c == ';') {
        return ':';
    } else if (c == '\'') {
        return '"';
    } else if (c == '[') {
        return '{';
    } else if (c == ']') {
        return '}';
    } else if (c == '-') {
        return '_';
    } else if (c == '1') {
        return '!';
    } else if (c == '7') {
        return '&';
    } else if (c == '9') {
        return '(';
    } else if (c == '0') {
        return ')';
    }
    return c;
}

char lowerCase(char c) {
    if (c >= 65 && c <= 90) {
        return tolower(c);
    } else if (c == '<') {
        return ',';
    } else if (c == '>') {
        return '.';
    } else if (c == ':') {
        return ';';
    } else if (c == '!') {
        return '1';
    } else if (c == '&') {
        return '7';
    } else if (c == '(') {
        return '9';
    } else if (c == ')') {
        return '0';
    } else if (c == '"') {
        return '\'';
    } else if (c == '{') {
        return '[';
    } else if (c == '}') {
        return ']';
    } else if (c == '_') {
        return '-';
    }
    return c;
}

bool needsShift(char c) {
    return !(c == lowerCase(c));
}

char getKeyChar(int keyCode) {
    if (keyCode == kVK_ANSI_A) {
        return 'a';
    } else if (keyCode == kVK_ANSI_B) {
        return 'b';
    } else if (keyCode == kVK_ANSI_C) {
        return 'c';
    } else if (keyCode == kVK_ANSI_D) {
        return 'd';
    } else if (keyCode == kVK_ANSI_E) {
        return 'e';
    } else if (keyCode == kVK_ANSI_F) {
        return 'f';
    } else if (keyCode == kVK_ANSI_G) {
        return 'g';
    } else if (keyCode == kVK_ANSI_H) {
        return 'h';
    } else if (keyCode == kVK_ANSI_I) {
        return 'i';
    } else if (keyCode == kVK_ANSI_J) {
        return 'j';
    } else if (keyCode == kVK_ANSI_K) {
        return 'k';
    } else if (keyCode == kVK_ANSI_L) {
        return 'l';
    } else if (keyCode == kVK_ANSI_M) {
        return 'm';
    } else if (keyCode == kVK_ANSI_N) {
        return 'n';
    } else if (keyCode == kVK_ANSI_O) {
        return 'o';
    } else if (keyCode == kVK_ANSI_P) {
        return 'p';
    } else if (keyCode == kVK_ANSI_Q) {
        return 'q';
    } else if (keyCode == kVK_ANSI_R) {
        return 'r';
    } else if (keyCode == kVK_ANSI_S) {
        return 's';
    } else if (keyCode == kVK_ANSI_T) {
        return 't';
    } else if (keyCode == kVK_ANSI_U) {
        return 'u';
    } else if (keyCode == kVK_ANSI_V) {
        return 'v';
    } else if (keyCode == kVK_ANSI_W) {
        return 'w';
    } else if (keyCode == kVK_ANSI_X) {
        return 'x';
    } else if (keyCode == kVK_ANSI_Y) {
        return 'y';
    } else if (keyCode == kVK_ANSI_Z) {
        return 'z';
    } else if (keyCode == kVK_Space) {
        return ' ';
    } else if (keyCode == kVK_Tab) {
        return '\t';
    } else if (keyCode == kVK_Return) {
        return '\n';
    } else if (keyCode == kVK_ANSI_Semicolon) {
        return ';';
    } else if (keyCode == kVK_ANSI_Comma) {
        return ',';
    } else if (keyCode == kVK_ANSI_Period) {
        return '.';
    } else if (keyCode == kVK_ANSI_Slash) {
        return '/';
    } else if (keyCode == kVK_ANSI_Quote) {
        return '\'';
    } else if (keyCode == kVK_ANSI_LeftBracket) {
        return '[';
    } else if (keyCode == kVK_ANSI_RightBracket) {
        return ']';
    } else if (keyCode == kVK_ANSI_Minus) {
        return '-';
    } else if (keyCode == kVK_ANSI_Equal) {
        return '=';
    } else if (keyCode == kVK_ANSI_0) {
        return '0';
    } else if (keyCode == kVK_ANSI_1) {
        return '1';
    } else if (keyCode == kVK_ANSI_2) {
        return '2';
    } else if (keyCode == kVK_ANSI_3) {
        return '3';
    } else if (keyCode == kVK_ANSI_4) {
        return '4';
    } else if (keyCode == kVK_ANSI_5) {
        return '5';
    } else if (keyCode == kVK_ANSI_6) {
        return '6';
    } else if (keyCode == kVK_ANSI_7) {
        return '7';
    } else if (keyCode == kVK_ANSI_8) {
        return '8';
    } else if (keyCode == kVK_ANSI_9) {
        return '9';
    }
    return -1;
}

int getKeyCode(char c) {
    c = tolower(c);
    if (c == 'a') {
        return kVK_ANSI_A;
    } else if (c == 'b') {
        return kVK_ANSI_B;
    } else if (c == 'c') {
        return kVK_ANSI_C;
    } else if (c == 'd') {
        return kVK_ANSI_D;
    } else if (c == 'e') {
        return kVK_ANSI_E;
    } else if (c == 'f') {
        return kVK_ANSI_F;
    } else if (c == 'g') {
        return kVK_ANSI_G;
    } else if (c == 'h') {
        return kVK_ANSI_H;
    } else if (c == 'i') {
        return kVK_ANSI_I;
    } else if (c == 'j') {
        return kVK_ANSI_J;
    } else if (c == 'k') {
        return kVK_ANSI_K;
    } else if (c == 'l') {
        return kVK_ANSI_L;
    } else if (c == 'm') {
        return kVK_ANSI_M;
    } else if (c == 'n') {
        return kVK_ANSI_N;
    } else if (c == 'o') {
        return kVK_ANSI_O;
    } else if (c == 'p') {
        return kVK_ANSI_P;
    } else if (c == 'q') {
        return kVK_ANSI_Q;
    } else if (c == 'r') {
        return kVK_ANSI_R;
    } else if (c == 's') {
        return kVK_ANSI_S;
    } else if (c == 't') {
        return kVK_ANSI_T;
    } else if (c == 'u') {
        return kVK_ANSI_U;
    } else if (c == 'v') {
        return kVK_ANSI_V;
    } else if (c == 'w') {
        return kVK_ANSI_W;
    } else if (c == 'x') {
        return kVK_ANSI_X;
    } else if (c == 'y') {
        return kVK_ANSI_Y;
    } else if (c == 'z') {
        return kVK_ANSI_Z;
    } else if (c == ' ') {
        return kVK_Space;
    } else if (c == '\t') {
        return kVK_Tab;
    } else if (c == '\n') {
        return kVK_Return;
    } else if (c == ';') {
        return kVK_ANSI_Semicolon;
    } else if (c == ',') {
        return kVK_ANSI_Comma;
    } else if (c == '.') {
        return kVK_ANSI_Period;
    } else if (c == '/') {
        return kVK_ANSI_Slash;
    } else if (c == '\'') {
        return kVK_ANSI_Quote;
    } else if (c == '[') {
        return kVK_ANSI_LeftBracket;
    } else if (c == ']') {
        return kVK_ANSI_RightBracket;
    } else if (c == '-') {
        return kVK_ANSI_Minus;
    } else if (c == '=') {
        return kVK_ANSI_Equal;
    } else if (c == '0') {
        return kVK_ANSI_0;
    } else if (c == '1') {
        return kVK_ANSI_1;
    } else if (c == '2') {
        return kVK_ANSI_2;
    } else if (c == '3') {
        return kVK_ANSI_3;
    } else if (c == '4') {
        return kVK_ANSI_4;
    } else if (c == '5') {
        return kVK_ANSI_5;
    } else if (c == '6') {
        return kVK_ANSI_6;
    } else if (c == '7') {
        return kVK_ANSI_7;
    } else if (c == '8') {
        return kVK_ANSI_8;
    } else if (c == '9') {
        return kVK_ANSI_9;
    }
    return -1;
}

int findKeycodeAfterIndex(NSArray *keyArray, int keyCode, int start) {
    
    int itemIndex = -1;
    int* itemIndexPtr = &itemIndex;
    
    [keyArray enumerateObjectsUsingBlock:^(id obj, NSUInteger index, BOOL * stop) {
        if ((int)index > start && [obj integerValue] == keyCode) {
            *itemIndexPtr = (int)index;
            *stop = YES;
        }
    } ];
    
    return itemIndex;
    
}

int findKeycode(NSArray *keyArray, int keyCode) {
    return findKeycodeAfterIndex(keyArray, keyCode, -1);
}

bool getClosedRange(NSArray *keyArray, NSRange* range) {
    int leftIndex = findKeycode(keyArray, kVK_ANSI_LeftBracket);
    if (leftIndex != -1) {
        int rightIndex = findKeycodeAfterIndex(keyArray, kVK_ANSI_RightBracket, leftIndex);
        if (rightIndex != -1) {
            range->location = leftIndex + 1;
            range->length = rightIndex - leftIndex - 1;
            return true;
        }
        return false;
    }
    return false;
}

void typeDelete(CGEventSourceRef src, CGEventTapProxy proxy, int count) {
    // Delete the number of characters that were in the source pattern
    // in addition to the left bracket
    for (int i = 0; i < count; i++) {
        CGEventRef downEvent = CGEventCreateKeyboardEvent(NULL, kVK_Delete, true);
        CGEventTapPostEvent(proxy, downEvent);
        CFRelease(downEvent);
        CGEventRef upEvent = CGEventCreateKeyboardEvent(NULL, kVK_Delete, false);
        CGEventTapPostEvent(proxy, upEvent);
        CFRelease(upEvent);
    }
}

void typeMessage(CGEventSourceRef src, CGEventTapProxy proxy, NSString *msg) {
    
    const char* targetCStr = [msg cStringUsingEncoding:NSASCIIStringEncoding];
    
    for (int i = 0; i < strlen(targetCStr); i++) {
        
        char c = targetCStr[i];
        // Flag for whether to hold down shift
        CGEventFlags flags = 0;
        if (needsShift(c)) {
            flags = flags | kCGEventFlagMaskShift;
        }
        int keyCode = getKeyCode(lowerCase(c));
        
        // Key down
        CGEventRef downEvent = CGEventCreateKeyboardEvent(src, keyCode, true);
        // CGEventSetFlags(downEvent, CGEventGetFlags(downEvent) | flags);
        CGEventSetFlags(downEvent, flags);
        CGEventTapPostEvent(proxy, downEvent);
        CFRelease(downEvent);
        
        // Key up
        CGEventRef upEvent = CGEventCreateKeyboardEvent(src, keyCode, false);
        // CGEventSetFlags(upEvent, CGEventGetFlags(upEvent) | flags);
        CGEventSetFlags(upEvent, flags);
        CGEventTapPostEvent(proxy, upEvent);
        CFRelease(upEvent);
        
    }
    
}

// Synthesize message from sequence of key presses and shifts
NSString* getMessage(NSArray *keyArray, NSArray *shiftArray) {
    NSMutableString *msg = [[NSMutableString alloc] init];
    [keyArray enumerateObjectsUsingBlock:^(id obj, NSUInteger index, BOOL * stop) {
        char c = getKeyChar((int)[obj intValue]);
        if ([[shiftArray objectAtIndex:index] boolValue]) {
            c = upperCase(c);
        }
        [msg appendFormat:@"%c", c];
    } ];
    return msg;
}

CGEventRef logKey(CGEventTapProxy proxy, CGEventType type, CGEventRef ref, void *refcon) {
    
    KeyPressData *kpData = (__bridge KeyPressData*)refcon;
    NSMutableArray *keyArray = kpData.keyPresses;
    NSMutableArray *shiftPositions = kpData.shiftPositions;
    NSArray *rules = kpData.rules;

    int keyCode = (int) CGEventGetIntegerValueField(ref, kCGKeyboardEventKeycode);
    
    // Ignore the following types of events:
    // * key ups
    // * special keys (shift, etc.)
    if (type == kCGEventKeyUp | type == kCGEventFlagsChanged) {
        return ref;
    } else if (keyCode == kVK_Delete) {
        if ([keyArray count] > 0) {
            [keyArray removeLastObject];
        }
        if ([shiftPositions count] > 0) {
            [shiftPositions removeLastObject];
        }
        return ref;
    }

    bool shiftDown = CGEventSourceKeyState(kCGEventSourceStateHIDSystemState, kVK_Shift);
    [keyArray addObject:[NSNumber numberWithInteger:keyCode]];
    [shiftPositions addObject:[NSNumber numberWithBool:shiftDown]];
    
    // Search for a regular expression pattern that matches ours (in our case, let's look
    // for {{ on either side, the same way that the Django templating engine does it,
    // so that this hopefully adapts to most languages that use brackets for blocks
    // The pattern will be pj {{ }}.  When we see this pattern, we get everythin inside
    // as the message.

    NSError *error = NULL;
    NSString *MACRO = @"pj \\{\\{\\s*(.*?)\\s*\\}\\}";
    NSRegularExpression *macroPatt = [NSRegularExpression regularExpressionWithPattern:MACRO options:NSRegularExpressionDotMatchesLineSeparators error:&error];
    if (error != NULL) {
        NSLog(@"Regex error: %@", error);
    }
    NSString *keyedMsg = getMessage(keyArray, shiftPositions);
    NSArray *matches = [macroPatt matchesInString:keyedMsg options:0 range:NSMakeRange(0, [keyedMsg length])];
    bool matchFound = (int)[matches count] >= 1;

    if (matchFound) {

        NSTextCheckingResult *match = [matches objectAtIndex:0];
        NSRange msgRange = [match rangeAtIndex:1];
        NSArray *keysBetween = [keyArray subarrayWithRange:msgRange];
        NSArray *shiftsBetween = [shiftPositions subarrayWithRange:msgRange];
        NSString *msg = getMessage(keysBetween, shiftsBetween);
        
        // Look for a rule that matches and type it in if it's there
        bool ruleFound = false;
        for (NSDictionary *rule in rules) {
            
            NSString *pattStr = [rule objectForKey:@"source"];
            NSError *error = NULL;
            NSRegularExpression *patt =
                [[NSRegularExpression alloc] initWithPattern:pattStr options:0 error:&error];
            if (error != NULL) {
                NSLog(@"Error building source pattern: %@", error);
            }
            NSLog(@"Patt str: %@", pattStr);
            
            if ((int)[patt numberOfMatchesInString:msg options:0 range:NSMakeRange(0, [msg length])] > 0) {
                ruleFound = true;
                NSLog(@"Match found: %@", pattStr);
                NSObject *tmplObj = [rule objectForKey:@"target"];
                // Templates can be specified as either strings, or arrays of lines (arrays of strings)
                NSString *tmpl = @"";
                if ([tmplObj isKindOfClass:[NSString class]]) {
                    tmpl = (NSString*)tmplObj;
                } else if ([tmplObj isKindOfClass:[NSArray class]]) {
                    tmpl = [(NSArray*)tmplObj componentsJoinedByString:@"\n"];
                }
                NSString *target = [patt stringByReplacingMatchesInString:msg options:0
                    range:NSMakeRange(0, [msg length]) withTemplate:tmpl];
                // NSLog(@"Replace with: %@", target);
                CGEventSourceRef src = CGEventSourceCreate(kCGEventSourceStateHIDSystemState);
                // Delete one fewer characters than macro match length, as the last character of
                // the macro will never be passed on my this event tap
                int charsToDelete = (int)[match range].length - 1;
                typeDelete(src, proxy, charsToDelete);
                typeMessage(src, proxy, target);
                CFRelease(src);
                break;
            }
            
        }
        
        // Clear out the stored keys so we start fresh with the next bracket
        [keyArray removeAllObjects];
        [shiftPositions removeAllObjects];
        
        // If a rule was matched, don't type the final bracket
        if (ruleFound) {
             return NULL;
        }
        
    }

    return ref;
    
}

// What we know about the current problem is
// 1. Delete works fine for everything
// 2. Writing additional characters for the input string appears to help flush things out (which would mean more characters to delete)
// 3. There is no relationship between the number of char in either the input or the output string and whether it prints
// 4. The phenomenon can be seen with plain ASCII characters
// 5. It's not based on the total number of preceding characters types (as we can put spaces before the bracket and it doesn't help but spaces inside of the braces sometimes do)

int main(int argc, const char * argv[]) {

    // TODO: replace this with a path to a resource instead of a full path to this rules file
    NSInputStream *inStream = [[NSInputStream alloc] initWithFileAtPath:@"/Users/andrew/Adventures/design/code/research/proto/p15/Keylogger/Keylogger/rules.json"];
    [inStream open];

    NSError *jsonError = NULL;
    NSArray *rules = [NSJSONSerialization JSONObjectWithStream:inStream options:0 error:&jsonError];
    if (jsonError != NULL) {
        NSLog(@"JSON reading error: %@", jsonError);
    }
    
    [inStream close];
    inStream = nil;
    
    KeyPressData *kpData = [[KeyPressData alloc] init];
    kpData.keyPresses = [NSMutableArray array];
    kpData.shiftPositions = [NSMutableArray array];
    kpData.rules = rules;
    void *kpDataPtr = (__bridge void*) kpData;
    
    // Listen for key down events
    CGEventMask mask = CGEventMaskBit(kCGEventKeyDown) |
        CGEventMaskBit(kCGEventKeyUp) |
        CGEventMaskBit(kCGEventFlagsChanged);
    
    // Create an event tap that
    // * listens for HID events before they enter the window server
    // * applies this tap before other taps at this location
    // * can both listen for and modify events
    // * listens for key down events
    CFMachPortRef portRef = CGEventTapCreate(
        kCGHIDEventTap,
        kCGHeadInsertEventTap,
        kCGEventTapOptionDefault,
        mask,
        &logKey,
        kpDataPtr);
    CGEventTapEnable(portRef, true);
    
    CFRunLoopSourceRef sourceRef = CFMachPortCreateRunLoopSource(
        kCFAllocatorDefault,
        portRef,
        0
    );
    
    CFRunLoopRef currentLoop = CFRunLoopGetCurrent();
    CFRunLoopAddSource(
        currentLoop,
        sourceRef,
        kCFRunLoopCommonModes
    );
    
    // Look up what CFRunLoopRun does, going forward
    CFRunLoopRun();
    
    return 0;
    
}
