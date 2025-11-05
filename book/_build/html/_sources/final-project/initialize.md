# Initialize GitHub repository

The goal of the activity this week is to:
   
   
   * Create a new GitHub repository for your final project

    
   * Practice pushing and pulling to the remote repository

   
   * Install necessary Python packages to carry out project


## Team leader: make a new Github repository

If you’re working in a group, pick a **project lead** to initiate and manage the **GitHub repository** (or repo). 

* Go to: https://github.com/


* Make a new repository by clicking the big green **New** button.  Come up with a short, descriptive repo name - try to avoid names like "finalproject", which won't make the project very memorable or searchable. 


* Set the access to **Public** (so instructors/other students can follow progress).


* Select to include a `README.md` and include a `.gitignore` file with a `Python` template.


Don’t stress too much about the specifics of the repo - these are not permanent, and you can always change repo names, or start over entirely (just copy and add existing files as a first commit). One of the goals here is to gain more experience using `git` for collaborative work and, early on, you're inevitably going to make some mistakes.

* When you're happy, click the green **Create repository** button.

## Team leader: add other team members to repository

The team leader now needs to add the others as collaborators and make sure they have permission to push changes to the repository.

* Click **Settings** from the top menu and --> **Collaborators** from the menu of the left


* Click the big green **Add people** button and add the other team members using their **GitHub usernames**

## Everyone: Add SSH key and install `git`

At this stage, we may need to setup **SSH (Secure Shell Protocol)**. We can do this by first generating a new **SHH key** following these [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac) 


Then add the new SSH key to our GitHub account following these [instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

Then install `git` by following these [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Everyone: Clone repository

Once we have generated a local SSH key and added it to our account, all team members should **clone** the repository to their local machine.

* Copy the **SSH URL** of the new repository by clicking the big green **<> Code** button

* Navigate to place in your file directory where you keep your coursework (e.g. `C:\Users\user\Documents`)

* `clone` the repository locally by running:

```bash
git clone git@github.com:<team-leader-username>/<project-repo-name>.git
```

```{note}
Where `<team-leader-username>` is the **team leader's** GitHub username and `<project-repo-name>` is the name of the new project repo. 
```

## Workflow

All **team members** should now have a local copy of the repository that includes an empty `README.md` file. 

* One team member can now replace the empty `README.md` file with the README that you produced in last week's activity and save the file. 

* Now **push** those changes to the remote repository by running:

```bash
git commit -a -m "added information to README"
git push
```

* Other team members can now download these changes to their local repository by running:

```bash
git pull
```

## Branching

To fully explore the power of GitHub, we recommend that students use a branching workflow. The learning curve is a little steeper than the centralized workflow but will provide a more complete introduction to git and GitHub. 

* **All team members** should create a their **own branch** by running:

```bash
git checkout -b xxx
```
where `xxx` is their name or something. 

* All team members should make changes to the `README.md`. Once they are finished, **commit** the changes and **push** to the remote repository using:

```bash
git commit -a -m "more edits to README"
git push --set-upstream origin xxx
```

## Pull request

* In GitHub.com, one of the team members should click the big green **Compare & pull request** button, then **Create pull request**, **Merge pull request**, and **Confirm merge**. 

```{note}
There are instructions for doing a pull request using command-line on this page.
```

The `README.md` should now be updated on the `main` branch. 


* Once your changes have been incorporated in the `main` branch it is good practice to clean up your repository. **All team members** should check back into `main`, pull the new edits from the remote, and **delete** the old branches. 

```bash
git checkout main
git pull
git branch -d xxx
```
 
* Repeat the steps above to contribute to the project.

##  Some tips for collaborating on group project

The best practice for collaborating on GitHub is to **avoid** situations where two people are independently **working on the same file**. When trying to push/pull changes to/from same origin branch, there will inevitably be **merge conflicts** that can be messy to untangle.

Collaboration is also a little more complicated with `Jupyter Notebooks` since running cells in the notebook will change execution count and output, even if the code and content appear identical. You are welcome to use other programs to write scripts (e.g. `Jupyter Lab` or `Spyder`). 

General recommendation - **split up** the project into multiple **smaller scipts**, and have each person work on different components. For example, you could have one script that ingests files, reduces/manipulates the data (e.g., reprojection), then writes new files out to disk in "analysis-ready" format. Then a second notebook reads in those data and does some analysis, creates some plots, etc. If you can pass things back and forth between group members like this, you'll avoid conflicts.

* Create subdirectories in your repo to store:
    * **notebooks** - contains scripts to complete project
    * **data** - contains small amount of data such as output of analyses. Just make sure filesizes are <20 MB and total number of files (<20 MB) is limited. Best practice is to store and share data on **Dropbox**. 
    * **doc** - for any additional documentation, static images/figures that you want to include in notebooks or markdown files, etc.

* Start adding and developing notebooks, code, markdown files, etc.

* Start with limited test case(s) for initial development and exploration:
    * Extract a small region of a large raster
    * If you need the entire raster, start with a downsampled version, then when you're happy with methods, run for native resolution
    * Start with a single timestep or subset of timesteps for time series analysis

* Don’t add unnecessary files to your repo (careful with `git add/commit`)

* Commit **early**, commit **often**, and use **branches**

*****************************

## Everyone: install a Python distribution

There are many ways to do this, but our *current* preferred option is described below. One advantage of the workflow described next is that it is cross-platform meaning that it should work on Windows, MacOS, and Linux operating systems. Some of the text here overlaps with the [intro to Python packaging](https://cleo-lab.github.io/gds-applications-site/course-info/python.html) page. 


As a reminder, a distribution is a collection of files that together allows us to build, package, and distribute a module. Since many software programs are written in Python, all computers have an internal **Python distribution** by default but it is usually an older version of Python (e.g. Python 2.7). 


Given that we require specific packages for geospatial data science, it is good practice to install a more modern Python distribution using [`Miniconda`](https://docs.conda.io/en/latest/miniconda.html).


Most students downloaded Python in Week 1 so can **skip this setep**. But, as a reminder, the latest version of Miniconda can be installed from the [dowload page](https://docs.conda.io/en/latest/miniconda.html). 

We can check that Python is installed by opening an **Anaconda Prompt (miniconda3)** (Windows) and entering:

```
where python
```

Or, on MacOS, open a **Terminal** and enter:

```
which python
```

We should see somthing like:

```
C:\Users\johnny\miniconda3\python.exe
```

Or:

```bash
/opt/miniconda3/bin/python
```

## Setup a virtual environment

It is good practice to create a new virtual environment for each new programming project (e.g. the final project for this class). A virtual environment allows us to install Python packages for one project without worrying about conflicts with packages of other projects. Python has built-in support for virtual environments using the `venv` module. A new environment can be created using the following command in an **Anaconda Prompt (miniconda3)** (Windows) or **Terminal** (macOS):

```
python -m venv .venv
```

```{note}
The dot in `.venv` means that it is a hidden file. `.venv` or `venv` are standard names for virtual environments.  
```

Next we need to activate the virtual environment. In Windows this can be achieved by running:

```
.venv\Scripts\activate
```

On macOS, run:

```bash
source .venv/bin/activate
```

## Install dependencies

We can install individual Python packages using [`pip`](https://pip.pypa.io/en/stable/). The syntax is `pip install xxx` where `xxx` is the package we want to install. It's often easier to install multiple packages at once using a text file, so that anyone else setting up the project will have exactly the same environment. 

To do this we can make a text file called `requirements.txt` using **Notepad** on Windows or **TextEdit** on MacOS, add the names of the packages for the project, and save it into our new project folder. 

We can install all the packages at once by running:

```
pip install -r requirements.txt 
```

```{note}
This could take between a few seconds to tens of minutes depending on how many packages need to be installed.
```

We can check that everything installed properly by first running:

```
python
```

Then:

```python
import numpy
```

If this runs without error, we are all good. If we get a `ModuleNotFoundError:`, we might check that the package was included in our `requirements.txt` file. 

```{note}
Exit the Python interpreter by pressing `Ctrl + Z` and then `Enter` in Windows or just `control + Z` in MacOS.
```

```{important}
There is no deliverable for this activity.
```