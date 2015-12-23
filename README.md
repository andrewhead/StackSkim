# Research Repository for PINABH

This is a repository of research files related to the **PINABH** project.
PINABH stands for Programmer Information Needs and Better Help.
Okay, the name is a work in progress.

To view the notes:

    brew install npm     # install npm
    npm install -g harp  # install harp, the Markdown server
    cd notes            
    ./runserver.sh       # this creates a documentation index and runs the server

Then go to `http://localhost:9000` in your browser.

The directories you find here contain different types of research artifacts:
* `eval/`: **evaluations**, or tests run to collect observations or evaluate hypotheses
* `proto/`: **prototypes**, systems we build that aren't big enough to be standalone
* `rel/`: **related work**, plans and findings from reviewing literature
* `vis/`: **vision documents**, where we plan out next steps for the projects
* `notes/`: **notes** written up to document the research process for evaluations, prototypes, related work, and vision documents.

When possible, documentation is written in Markdown.
This improves the maintainability of the documentation and makes it editable in a variety of editors.

## Running experiment code or prototypes

In general, you should be able to `cd` into the directory for an evaluation or prototype.
Then download the dependencies specific to that project.

    pip install -r reqs.txt

See the experimental notes for that evaluation for how to run it.

## Contributing

Develop with a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) when possible.
You should have a separate virtual environment for each prototype or evaluation.
When you commit your work, save the requirements for others to install later:

    pip freeze > reqs.txt

## Contributors

* Andrew Head
* Austin Le
