#!/usr/bin/env python
# coding: utf-8

# # Getting started with Python and GitHub
# 
# **Objectives:**
#    * Sign-up for a **GitHub** account
#    * Fork the course repository to access the materials
#    * Install a **Python** distribution using **Anaconda**
#    * Make a new Python **environment** using <code>conda</code>
#    * View the first assignment as a <code>jupyter notebook</code>

# ## Join the slack channel
# 
# Students should have received an email (via Canvas) for an invite to the course Slack workspace.
# 
# If you’re confused or uncertain about something in the lab, please ask or post a question/comment on the relevant Slack channel for the lab (e.g., #lab01). 

# ### Complete background survey
# 
# If you haven't already, please complete the background survey which can be found on the course Canvas page.

# ### Sign-up for a GitHub account and fork the course repository
# 
# If you already have a GitHub account, you can skip this step. If not, create a new GitHub account using your <code>@uoregon.edu</code> email address [here](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home). We recommend that you apply for the free "edu" account upgrade (https://education.github.com/discount_requests/new) which will allow you to create unlimited number of private repos with unlimited collaborators.
# 
# Once signed in to GitHub.com browse to <code>https://github.com/JohnnyRyan1/geospatial-data-science</code> and click **Fork** from the upper-right menu. This copies all the course materials to your GitHub account and allows you to upload assignments without affecting the original repository.

# ### Install <code>git</code> and clone the course repository
# 
# In this course we will use `git` to upload assignments, share code, and collaborate on class projects. Linux and Mac users can install <code>git</code> as a command line tool following [these instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). I recommend that Windows users (and Mac users who prefer a graphical user interface) install [GitHub Desktop](https://desktop.github.com/). 
# 
# Once <code>git</code> is installed, we can clone the course repository from the command line by running:
# 
# `git clone https://github.com/<your-username>/geospatial_data_science`
# 
# Where ```<your-username>``` is your GitHub username. *Note that you should navigate to your coursework folder before running this command*
# 
# In GitHub Desktop, click **Clone a repository from the Internet**, enter `https://github.com/<your-username>/geospatial_data_science` as the **URL**, choose a **local path** where you keep your coursework (e.g. `C:\Users\your_name\Documents`) and click **Clone**.

# ###  Install Anaconda
# 
# In order to execute Python code in the notebooks, we will need to install a Python distribution with the necessary packages. Ananconda is already installed on the SSIL lab computers but we can also get it on a laptop from this website [Anaconda Individual Edition](https://www.anaconda.com/products/individual).

# ###  Make a new environment
# 
# Once Anaconda is installed, we will create an environment which contains all the packages required to run the code in each lab. We will find this environment file (e.g. <code>environment.yml</code>) in each lab folder of the cloned repository. 
# 
# *********
# 
# For Linux and Mac users, we can create the environment for **Lab 1** by navigating to the **labs/lab1** folder in the cloned repository using the terminal and running the following:
# 
# <code>conda env create -f environment.yml</code>
# 
# This will create a new environment called **lab1**. To activate this environment, type:
# 
# <code>conda activate lab1</code>
# 
# To deactivate this environment, type:
# 
# <code>conda deactivate</code>
# 
# *************
# 
# For Windows users, open **Anaconda Navigator**, launch a **CMD.exe Prompt**, navigate to **labs/lab1** folder in cloned repository, and run the following:
# 
# <code>conda env create -f environment.yml</code>
# 
# To activate this environment, type:
# 
# <code>conda activate lab1</code>
# 
# To deactivate this environment, type:
# 
# <code>conda deactivate</code>
# 
# More information about managing environments can be found here: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

# ### View the assignments
# 
# Now that we have the required packages installed (and the lab1 environment activated), the notebooks can be viewed using the [jupyter notebook](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html) application. Navigate to the <code>/geospatial-data-science/labs/lab1/</code> and open the first assignment by running:
# 
# <code>jupyter notebook 01b_submitting_assignments.ipynb</code>
# 
# Windows users should be able to do this from the **CMD.exe Prompt** or by clicking the `jupyter notebook` icon in **Anaconda Navigator**, navigate to the repository and open the lab1 notebook.
# 
# *Note that if you browse directly to the notebooks on GitHub, they might not display as intended.*

# In[ ]:




