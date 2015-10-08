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
    
    int keyCode = (int) CGEventGetIntegerValueField(ref, kCGKeyboardEventKeycode);
    NSMutableArray *keyArray = (__bridge NSMutableArray*)refcon;
    [keyArray addObject:[NSNumber numberWithInteger:keyCode]];
    
    int leftIdx = findKeycode(keyArray, kVK_ANSI_LeftBracket);
    if (leftIdx != -1) {
        int rightIdx = findKeycodeAfterIndex(keyArray, kVK_ANSI_RightBracket, leftIdx);
        if (rightIdx != -1) {
            CGEventRef keyEvent = CGEventCreateKeyboardEvent(NULL, kVK_ANSI_KeypadPlus, true);
            CGEventTapPostEvent(proxy, keyEvent);
            [keyArray removeAllObjects];
        }
    }

    return ref;
    
}

int main(int argc, const char * argv[]) {

    NSMutableArray *arr = [NSMutableArray array];
    void *arrData = (__bridge void*) arr;

    // TODO: replae this with cleaner code for reading
    NSInputStream *inStream = [[NSInputStream alloc] initWithFileAtPath:@"/Users/andrew/Adventures/design/code/research/proto/p15/Keylogger/Keylogger/rules.json"];
    [inStream open];

    NSError *jsonError;
    NSArray *rules = [NSJSONSerialization JSONObjectWithStream:inStream options:0 error:&jsonError];
    /*
    char msgBuff[128];
    [[jsonError localizedDescription] getCString:msgBuff maxLength:128 encoding:NSASCIIStringEncoding];
    NSLog(@"Error code: %d", (int)[jsonError code]);
    NSLog(@"Error: %s", msgBuff);
     */
    
    for (NSDictionary *rule in rules) {
        NSLog(@"Source: %@", [rule objectForKey:@"source"]);
        NSLog(@"Target: %@", [rule objectForKey:@"target"]);
    }
    
    /*
    NSArray *keys = [rules keysSortedByValueUsingSelector:@selector(compare:)];
    for (NSString *key in keys) {
        char keyBuff[128];
        [key getCString:keyBuff maxLength:128 encoding:NSASCIIStringEncoding];
        NSLog(@"Key: %s", keyBuff);
    }
    */
    
    [inStream close];
    inStream = nil;
    
    // Listen for key down events
    CGEventMask mask = CGEventMaskBit(kCGEventKeyDown);
    
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
        arrData);
    
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
