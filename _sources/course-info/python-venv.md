# Install Python using `venv` and `pip`

A second option is to use `venv`, a built-in Python package that supports virtual environments. We can create a virtual environment running the following in a a command prompt (or Terminal): 

```
python3 -m gds .venv
```

This creates a new environment called `gds` in the `.venv` folder, which is where all the project dependencies will be installed. Next we will activate the virtual environment, by running the following in the command prompt (or Terminal):

```
source .venv/bin/activate
```

## Install requirements

In this always install project dependencies with `pip`, which downloads them from the Python package index at pypi.org. However, it's best practice to declare dependencies in a requirements.txt file and install from that file, so that anyone else setting up the project will end up with the same dependencies.

I create the requirements.txt file and seed it with any packages I know I need:

