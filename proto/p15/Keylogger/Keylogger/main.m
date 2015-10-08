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
    NSArray *rules;
    bool shiftDown;
}
@property(nonatomic, readwrite) NSMutableArray *keyPresses;
@property(nonatomic, readwrite) NSArray *rules;
@property(nonatomic, readwrite) bool shiftDown;
@end

@implementation KeyPressData

@synthesize keyPresses;
@synthesize rules;
@synthesize shiftDown;

-(id)init {
    self = [super init];
    shiftDown = false;
    return self;
}

@end

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
    } else if (keyCode == kVK_ANSI_Quote) {
        return '"';
    } else if (keyCode == kVK_ANSI_1) {
        return '1';
    }
    return -1;
}

int getKeyCode(char c) {
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
    } else if (c == '"') {
        return kVK_ANSI_Quote;
    } else if (c == '1') {
        return kVK_ANSI_1;
    }
    return -1;
}

int findKeycodeAfterIndex(NSMutableArray *keyArray, int keyCode, int start) {
    
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

int findKeycode(NSMutableArray *keyArray, int keyCode) {
    return findKeycodeAfterIndex(keyArray, keyCode, -1);
}

CGEventRef logKey(CGEventTapProxy proxy, CGEventType type, CGEventRef ref, void *refcon) {
    
    KeyPressData *kpData = (__bridge KeyPressData*)refcon;
    NSMutableArray *keyArray = kpData.keyPresses;
    NSArray *rules = kpData.rules;
    
    int keyCode = (int) CGEventGetIntegerValueField(ref, kCGKeyboardEventKeycode);
    [keyArray addObject:[NSNumber numberWithInteger:keyCode]];
    
    int leftIdx = findKeycode(keyArray, kVK_ANSI_LeftBracket);
    if (leftIdx != -1) {
        
        int rightIdx = findKeycodeAfterIndex(keyArray, kVK_ANSI_RightBracket, leftIdx);
        if (rightIdx != -1) {
 
            NSArray *keysBetween;
            NSRange range;
            range.location = leftIdx + 1;
            range.length = rightIdx - leftIdx - 1;
            NSMutableString *msg = [[NSMutableString alloc] init];
            
            keysBetween = [keyArray subarrayWithRange:range];
            for (NSNumber *num in keysBetween) {
                char c = getKeyChar((int)[num intValue]);
                [msg appendFormat:@"%c", c];
            }
            
            for (NSDictionary *rule in rules) {
                if ([[rule objectForKey:@"source"] compare:msg] == NSOrderedSame) {
                    
                    // Delete the number of characters that were in the source pattern
                    for (int i = 0; i < (int)[msg length]; i++) {
                        CGEventRef deleteEvent = CGEventCreateKeyboardEvent(NULL, kVK_Delete, true);
                        CGEventTapPostEvent(proxy, deleteEvent);
                    }
                    
                    // Generate all of the characters in the target pattern
                    NSString *target = [rule objectForKey:@"target"];
                    const char* targetCStr = [target cStringUsingEncoding:NSASCIIStringEncoding];
                    for (int i = 0; i < strlen(targetCStr); i++) {
                         CGEventRef keyEvent = CGEventCreateKeyboardEvent(NULL, getKeyCode(targetCStr[i]), true);
                         CGEventTapPostEvent(proxy, keyEvent);
                    }

                }
            }
            NSLog(@"%@", msg);
            [keyArray removeAllObjects];
        }
        
    }

    return ref;
    
}

int main(int argc, const char * argv[]) {

    NSMutableArray *arr = [NSMutableArray array];

    // TODO: replace this with a path to a resource instead of a full path to this rules file
    NSInputStream *inStream = [[NSInputStream alloc] initWithFileAtPath:@"/Users/andrew/Adventures/design/code/research/proto/p15/Keylogger/Keylogger/rules.json"];
    [inStream open];

    NSError *jsonError;
    NSArray *rules = [NSJSONSerialization JSONObjectWithStream:inStream options:0 error:&jsonError];
    
    [inStream close];
    inStream = nil;
    
    KeyPressData *kpData = [[KeyPressData alloc] init];
    kpData.keyPresses = arr;
    kpData.rules = rules;
    void *kpDataPtr = (__bridge void*) kpData;
    
    // Listen for key down events
    CGEventMask mask = CGEventMaskBit(kCGEventKeyDown) | CGEventMaskBit(kCGEventKeyUp);
    
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
    
    NSLog(@"Hello, World!");
    
    while (true) {}
    
    return 0;
    
}
