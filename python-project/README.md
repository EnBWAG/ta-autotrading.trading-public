Best Practise to setup a simple Python `3.11` application project.

If you want a library project which produces a Python package, then this is not for you.

Prerequisite is that you have Python installed under `MY_PYTHON_FOLDER` and a bash-like shell. On MS-Windows we recommend the `git bash`.

# Setup Virtual Environment

You have to do this once.

````
MY_PYTHON_FOLDER=***
MY_VENV_FOLDER=.venv
$MY_PYTHON_FOLDER/python -m venv $MY_VENV_FOLDER
````

# Activate Virtual Environment

MS-Windows
````
source $MY_VENV_FOLDER/Scripts/activate
````

Linux
````
source $MY_VENV_FOLDER/bin/activate
````

# Install Packages

You have to do this once initially and every time the requirements change.

````
# Do activate first!
pip install -r requirements.txt
````

# Execute Packages

````
# Do activate first!
python -m package_a arg1 arg2
-> Arguments for package_a are ['arg1', 'arg2']

python -m package_b
-> Cypher is b'gAAA***'
````

# Setup Dependency Management

This is for the dependencies/requirements manager. Your goal is to provide [reproducable builds](https://reproducible-builds.org).

You have to declare the top-level dependencies of your application in [requirements.in](requirements.in).
You *do not* declare all transitive dependencies in [requirements.txt](requirements.txt).
There are tools which do that for you. We opinionate [pip-tools](https://pypi.org/project/pip-tools).

Install `pip-tools` once.

````
# Do activate first!
pip install pip-tools
````

Then each time your top-level dependencies change, run

````
# Do activate first!
pip-compile requirements.in
git commit -m'change dependency XY' requirements.txt
````

Yes, even though [requirements.txt](requirements.txt) is generated, it is part of your repository and must be commited.

Do you know why this is necessary?

# Maintenance Tasks

From time to time you may update your tools with

````
python -m pip install -U pip pip-tools
````

# Design Decisions

TODO: Discuss advanced topics such as Python Packaging.
