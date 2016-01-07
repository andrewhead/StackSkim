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

### Follow This Development Workflow

1. Create a new branch for doing your work: `git checkout -b <branchname>`
2. Do your local work and commit.  All new features or bug fixes should be accompanied by tests.
3. Run the test suite to make sure everything still passes
4. Push your branch
4. Submit a pull request to merge into master ([see here](https://help.github.com/articles/using-pull-requests/)).  Assign the pull request to someone else on the team who should verify the style and design choices of your code.
6. Respond to any comments you get from reviewers
7. Once your pull request is accepted, merge your pull request into master
8. Check out the master branch and verify that all tests still pass

### Run Code In a Virtual Environment

Develop with a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) when possible.
You should have a separate virtual environment for each prototype or evaluation.
When you commit your work, save the requirements for others to install later:

    pip freeze > reqs.txt

### Check the Style of Your Code Against Some Standard

In general, to improve the readability of your code, write it according to some standard.
Your Python code should be checked with `flake8`, with a line length of 100 characters.
You can run the `flake8` check on all code in the current directory and its sub-directories like so:

    pip install flake8
    flake8 --max-line-length=100 .

Run this check before you push your feature or your reviewer will ask you to when they review.

## Contributors

* Andrew Head `<andrewhead@eecs.berkeley.edu>`
* Austin Le `<austinhle@berkeley.edu>`
