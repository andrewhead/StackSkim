# Prototype 11: Getting Regexper to run on a server

## Overview

### Purpose

To have the regular expression tutoron fulfill its role in the ecosystem, it should be able to assemble SVGs on the server and send them pre-computed back to the client.  This prototype investigates how we can do that.  This is an implementation prototype.

### Summary

The first reliable and quick-to-implement way we have discovered for generating SVGs of regular expression visualizations is to query a Regexper page in a Firefox browser (which can be headless) and scrape the SVG contents.

## Procedure

### Use case

A browser sends a query to localhost `127.0.0.1:8000` with the parameter `patt=[A-Z]+`.  It receives back an SVG created by Regexper that can be displayed on a webpage.

### Construction

We add the Regexper source as a submodule from [its Github page](https://github.com/javallone/regexper-static).  By going into its directory and running `npm install`, we fetch all of the dependencies listed in the `package.json` file.  Then we test what happens when we try to render on a non-existent webpage (e.g., just try to execute the code).

## Notes

### Observations

We find that there are two viable alternatives right now for generating visualizations of regular expressions on demand.

#### Scrape the SVG for the Regex from Regexper accessed in the browser

Despite our best efforts, Regexper currently needs to:
* Perform rendering on a *real* HTML document
* Perform this after page load with additional button presses, or properly render after receiving a regular expression as part of the ID tag.

As utilities like `requests` do not execute Javascript, we cannot rely on these scraping utilities to fetch the SVG.

Meanwhile, other utilities like `dryscrape` and the `PhantomJS` web driver for Selenium, while they mock the browser and can execute Javascript, fail to properly load the SVG (the page just gets wiped blank after the "Display" button is hit).

The one reliable method that we have found is to use the Firefox Selenium web driver.  After just `get`ting the page, with the regex pattern specified as the target, the SVG is fully rendered in the page.

This will mean that when running on OSX, we'll need to have a Firefox browser open for our regular expression server.

However, on Ubutunu servers, it's well established that you can [start a virtual frame buffer](http://www.alittlemadness.com/2008/03/05/running-selenium-headless/) and have Firefox open on a virtual display.  I have tested this out and verified that it works.

#### Use an alternate source for visualizations

[Regulex](https://jex.im/regulex/?re=^%28a|b%29*%3F%24#!embed=false&flags=&re=^%28a|b%29*%3F%24) is another site that offers similar visualizations of regular expressions to Regexper.  The color theme and fonts are more eccentric, so these visualizations don't look as nice.

However, Regulex allows you to embed these visualizations arbitrarily, by setting `embed` to `true` in the Query string [(example)](https://jex.im/regulex/?re=^%28a|b%29*%3F%24#!embed=false&flags=&re=^%28a|b%29*%3F%24).

After some StackOverflow checking up, it seems like there is not yet an easy way with CSS alone to make iframes grow to fit their entire content.  Because of the initial visual eccentricity and difficulty of getting the iframe to fit with our current source without script-level adjustment, we elect to go with the first alternative now.
