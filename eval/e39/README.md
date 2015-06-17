To run this, follow these steps:

# To Download the Test Tutorials

Only peform these steps if you are trying to get a fresh set of tutorials to run tests on.

Download all tags

    ./so_tags.py --init

Get a list of tutorials from Google that use the StackOverflow tags

    ./google_tutorials.py --init

Fetch all of the pages listed from Google

    ./fetch_tutorials.py

If you are just repeating tests that have already been performed, you do not have to
download this data again.  Instead, you get access to the Dropbox folder for this
and mount it as the folder pages/

# To Capture Test Data for Explainable Region Detection

To collect region detections and their ground truth, you need to run your own copy of
the Tutorons server, and use Firefox to mark up the ground truth regions where regions
*should* be detected.  To do so, follow these steps:

Build and install the Firefox plugin for copying a selection's location to the clipboard as tab-separated values

    cd selection-addon
    jpm xpi
    # Start the Firefox browser and make sure you have automatic extension installation
    wget --post-file=\@selection-addon.xpi http://localhost:8888/;

Start a local copy of the Tutorons server.  You can get a copy of the server from
https://github.com/andrewhead/tutorons-server.

    cd <server-directory> && ./rundevserver

Start the server logger to capture all regions automatically extracted.
regions.tsv will store all the regions that the Tutorons extract

    ./server_logger.py <server-directory>/.regions.log > regions.tsv

Visit all of the test pages one by one by running:

    ./openall.sh

For each page, find an explainable region that should be detected.  Select the full
text of an explainable region with your mouse.  A selector to the text and its range in 
that selector will be copied to the clipboard as TSV, with the following columns:

* index of starting character
* index of ending character
* selector that points to the element containing the range
* URL of the site where the range was found
* start offset of the range in the full HTML page where the selection was made
* end offset of the range in the full HTML page where the selection was made

Note that as we don't know what element the Tutoron will find the code in, the
selection plugin for the browser copies the offsets within *all container elements*
where the text could have been found.  Each one is copied as a separate row.