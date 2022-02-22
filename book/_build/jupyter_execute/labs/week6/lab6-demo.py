#!/usr/bin/env python
# coding: utf-8

# # Collaborating on GitHub
# 
# **Objectives:**
#    * Form teams and designate a team leader
#    
#    
#    * Create a new GitHub repository for final project
#    
#    
#    * Choose a GitHub workflow that works for all team members
#   
# 
#    * Prepare and submit an outline of your group's final project

# ### Team leader: make a new Github repository
# 
# If you’re working in a group, pick a **project lead** to initiate and manage the repo. 
# 
# 
# * Go to: https://github.com/
# 
# 
# 
# * Click the big green **New** button and follow instructions on the left side of page. Come up with a clever, descriptive repo name - try to avoid names like "finalproject", which won't make it very searchable. 
# 
# 
# 
# * Set the access to **Public** (so other students can follow progress).
# 
# 
# 
# * Select to include a `README.md` and include a `.gitignore` file with a `Python` template.
# 
# 
# Don’t stress too much about the specifics of the repo - these are not permanent, and you can always change repo names, or start over entirely (just copy and add existing files as a first commit). One of the goals here is to gain more experience using `git` for collaborative work and, early on, you're inevitably going to make some mistakes.

# ### Team leader: add other team members to repository
# 
# The team leader now needs to add the others as collaborators and make sure they have permission to access and commit. 
# 
# * Click **Settings** --> **Collaborators** from menu on the left
# 
# 
# * Click the big green **Add people** button and add the other team members using their **GitHub usernames**

# ### Everyone: clone repository
# 
# All team members should now go to GitHub Desktop, click **File** --> **Clone repository...**, enter `https://github.com/<team-leader-username>/<project-repo-name>` as the **URL** where ```<team-leader-username>``` is the **team leader's** GitHub username and ```<project-repo-name>``` is the name of the new project repo. 
# 
# Choose a **Local path** where you keep your coursework (e.g. `C:\Users\your_name\Documents`) and click **Clone**.
# 
# Notice that in the top left that **Current repository** is now set to `project-repo-name`. Depending on if we're working on our projects or lab assignments, we'll need to switch between this and `geospatial-data-science`.

# ------
# 
# ### Create a new Slack channel for discussion:
# 
# * Click **"+"** icon next to **Channels** list in the Slack sidebar -> **"Create a channel"**
# * Add your project name
# * Invite your team members Slack members
# 
# --------

# ## Centralized workflow in GitHub Desktop
# 
# * To contribute to the repo, **team members** should make a new file called `README_XX.md` where `XX` are the initials of the team member. 
# 
# 
# * When the team member is finished with thir edits to `README_XX.md`, they can go to **GitHub Desktop**, include a **Summary** of the changes, **Commit to main** and then click **Push origin** button.
# 
# 
# * **Team leader** can then go to **GitHub Desktop**, click **Fetch origin** and **Pull origin** to retrieve the changes that the team members made to their local environment. 
# 
# 
# * **Team leader** can then add useful text from `README_XX.md` to the main file (e.g. `README.md`). Once they are finished they can **delete** `README_XX.md`, go to **GitHub Desktop**, include a **Summary** of the changes, click **Commit to main** and then **Push origin** button.
# 
# 
# * **Team members** can then go to **GitHub Desktop**, click **Fetch origin** and **Pull origin** to retrieve the changes that the team leader made. Repeat the steps above to contribute to the project.
# 
# 

# ----------
# 
# ### Some tips for the centralized workflow
# 
# * Only the team leader should edit the main files (e.g. `README.md`)
# 
# 
# * Team members should edit their own versions (e.g. `README_XX.md`)
# 
# 
# * **Fetch** and **pull** regularly to avoid conflicts
# 
# 
# ---------

# ## Feature branch workflow in GitHub Desktop
# 
# If you feel comfortable with `GitHub`, you are welcome to use a more standard branching workflow.
# 
# 
# ### Workflow 
# 
# * In GitHub Desktop, **all team members** should create a their own branch by clicking the drop-down menu called **Current branch**, typing a name for their branch (e.g. `xx_branch`), click the big blue **Create new branch** button and **Create branch**
# 
# 
# * All team members should publish `xx_branch` to main repo by clicking the big blue **Publish branch** button
# 
# 
# * All team members can make changes to `README.md`. Once they are finished, go back to **GitHub Desktop**, include a **Summary** of the changes, click **Commit to `xx_branch`** and then **Push origin** button.
# 
# 
# * In GitHub Desktop, click the big blue **Create Pull Request** button which should take you to GitHub.com where you can click **Create pull request**.
# 
# 
# * The **team leader** can then go to `https://github.com/<team-leader-username>/<project-repo-name>`, click **Pull requests** from the top menu, click on the open pull request. If there are no conflicts, the team leader can click **Merge pull request** and **Confirm merge**.
# 
# 
# * The `README.md` should now be updated on the `main` branch. 
# 
# 
# * Once your changes have been incorpotated in the `main` branch it is good practice to clean up your repository by **deleting** the old branch (e.g. `xx_branch`).
#  
# 
# * Before starting new work, **all team members** should first click the **Fetch origin** button to check for new changes. 
# 
# 
# * Repeat the steps above to contribute to the project.

# -------------
# 
# ### Some tips for the feature branch workflow
# 
# 
# * Remember to **stay** on your own branch
# 
# 
# * Remember to **fetch** changes before making a new branch and starting work
# 
# 
# * If the changes in your branch conflict with another team member's branch, you can still **Create a pull request**. The **team leader** should click **Resolve conflicts**, decide what to keep and what discard and click **Mark as resolved** and **Commit merge**. The team leader can then click **Merge pull request** and **Confirm merge**
# 
# --------

# ## Feature branch workflow in command line
# 
# It seems like most people in the class are using GitHub Desktop. But if your team would like to use the command line, the steps are basically the same. There are some useful instructions here: https://icesat-2hackweek.github.io/learning-resources/projects/example_workflow/ and https://blog.scottlowe.org/2015/01/27/using-fork-branch-git-workflow/. The instructor and TA would also be happy to help get a workflow started. 

# ###  Some tips for collaborating on group project
# 
# Best practice for collaborating on GitHub is to **avoid** situations where two people are independently **working on the same script**. When trying to push/pull changes to/from same origin branch, there will inevitably be **merge conflicts** that can be messy to untangle.
# 
# Collaboration is also a little more complicated with `Jupyter Notebooks` since running cells in the notebook will change execution count and output, even if the code and content appear identical. You are welcome to use other programs to write scripts (e.g. `Jupyter Lab`). 
# 
# General recommendation - **split up** the project into multiple **smaller scipts**, and have each person work on different components. For example, you could have one script that ingests files, reduces/manipulates the data (e.g., reprojection), then writes new files out to disk in "analysis-ready" format. Then a second notebook reads in those data and does some analysis, creates some plots, etc. If you can pass things back and forth between group members like this, you'll avoid conflicts.

# ## Task 1: prepare a README (40 points)
# 
# The `README.md` file in your new repo will serve as the landing page for your project. You can continue to update it as your project evolves, but for now, please prepare a basic project outline.  
# 
# Review the [markdown cheat sheet](https://www.markdownguide.org/basic-syntax/) and use some basic headings, bulleted/numbered lists, and other formatting to organize your outline. We recommend using a **markdown editor** such as [MacDown](https://macdown.uranusjr.com/) for MacOS or [Ghostwriter](https://wereturtle.github.io/ghostwriter/download.html) for Windows.
# 
# Please include the following in `README.md`:
# 
# * Project Title
# * Name(s) of individual or team members
# * Short 1-2 sentence summary
# * Problem statement, question(s) and/or objective(s)
# * Datasets you will use (with links, if available)
# * Tools/packages you’ll need
# * Planned methodology/approach
# * Expected outcomes
# * Any other relevant information, images/tables, references, etc.
# * References
# 
# That may sound like a lot, but some of these items should only be 1-2 sentences, others can be short lists. Consider this the start of your final report. 
# 
# We would like to see at **least one commit** from **each group member** at this phase of the project, even if it is as simple as adding their name to the `README.md` file. 

# ## Task 2: push all changes to GitHub and submit README as a pdf to Canvas (10 points)
# 
# The markdown editors should be able to export `.md` files as `.pdf`

# ### Some notes for final projects
# 
# 
# * Start early! 
# 
# 
# * Create subdirectories in your repo to store:
#     * **notebooks** - contains scripts to complete project
#     * **data** - contains small amount of data such as output of analyses. Just make sure filesizes are <20 MB and total number of files (<20 MB) is limited. Best practice is to store and share data on **Dropbox**. 
#     * **doc** - for any additional documentation, static images/figures that you want to include in notebooks or markdown files, etc.
# 
# 
# * Start adding and developing notebooks, code, markdown files, etc.
# 
# 
# * Start with limited test case(s) for initial development and exploration:
#     * Extract a small region of a large raster
#     * If you need the entire raster, start with a downsampled version, then when you're happy with methods, run for native resolution
#     * Start with a single timestep or subset of timesteps for time series analysis
# 
# 
# * Don’t add unnecessary files to your repo (careful with `git add/commit`)
# 
# 
# * Commit **early**, commit **often**
