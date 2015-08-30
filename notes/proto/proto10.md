# Prototype 10: Node.js server

## Overview

### Purpose

We create a simple Node.js server that is returns HTML with a bolded version of a string that is passed via a request.

### Summary

We build a Node.js server that can transform a time input as a string into another format.

## Procedure

### Use case

John can't recall how to bold a string in HTML.  He has a local server running that will do this for him efficiently.  So he makes an AJAX query using the jQuery library:

    function makeCall(text) {
        $.get(
            'http://localhost:8000/bolden', 
            {'text': text},
            function(data) { console.log(data); }
        );
    }

After testing with `makeCall('hello')` he receives back the response `<p><strong>hello</strong></p>`.

### Construction

We build an example server `example.js` using the tutorial [here](https://nodejs.org/) for setting up a Node.js server.

Next, I want to create a URL that receives text, constructs a DOM using Javascript `document` methods, and then return a rendering of the HTML as text.  I follow the NodeSchool [`learnyounode`](https://github.com/workshopper/learnyounode) tutorial.

See `p10/nodeschool/p13.js` for an example of a server that listens for a request, matches the path to an endpoint, checks on the input arguments, and returns a response.  This involves using the `http` library to initialize a server, and the `url` module to parse the URL.

### Expected Outcome

John receives the exact string he expected and can make these calls in a few milliseconds each.

