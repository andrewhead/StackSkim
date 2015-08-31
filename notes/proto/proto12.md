# Prototype 12: Wrapper around Regexper Server

## Overview

### Purpose

Scrape an SVG from a webpage using a Selenium web driver for Firefox, triggered through the node package for `selenium-webdriver`.  This will allow us to have NPM run a lightweight, always-running endpoint for fetching SVGs for regular expressions.  This is an implementation prototype.

### Summary

We successfully retrieve an SVG for a Regex from a wrapper server around a local clone of Regexper.

## Procedure

### Construction

We install the [`selenium-webdriver`](https://www.npmjs.com/package/selenium-webdriver) module.  Then, using the `http` and `url` core modules of Node.js, we can parse incoming URLs for a regular expression pattern, and forward this as the "target" for the Regexper page.  We use the Selenium web driver's asynchronous callbacks as documented [here](https://code.google.com/p/selenium/wiki/WebDriverJs) to fetch the HTML of the container of the SVG, and then send this SVG back to the original requester.

#### Replication

Go to `proto/p11/regexper-static` and start the server by running `gulp`.

Then start the wrapper server by going to `proto/p12` and running

    node webdriver.js 8000

Finally, fetch the SVG for a pattern as follows:

    wget http://127.0.0.1:8000/?pattern=hi

### Goals

Given a query to `127.0.0.1:8000`, with the parameter `pattern` set to `[A-Z]+` we want to receive a response containing an SVG that was retrieved from the official [Regexper page](http://regexper.com).
