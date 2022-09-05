#!/usr/bin/env python
# coding: utf-8

# # Instructions for submitting assignments
# 
# **Objectives:**
#    * Write a Python script in <code>spyder</code>
#    * Add the script to your answers notebook along with some text and an image
#    * Submit answers notebook in <code>.ipynb</code> format using GitHub
#    * Submit answers notebook in <code>.pdf</code> format via Canvas

# ## Write a short script using Spyder
# 
# So now that we have things up-and-running, we can start writing short scripts. Click on the cell below and click **Run** from the menu above. 

# In[3]:


import numpy as np
a = 3
b = 2
c = np.multiply(a, b)
print(c)


# Running code interactively in these notebooks will be the main way of demonstrating different concepts in this course. But sometimes it is easier to write and edit code in an IDE (integrated development environment) such as <code>spyder</code> which was installed when we created the **lab1** environment.  
# 
# Linux and Mac users can open the IDE by typing <code>spyder</code> in a terminal. 
# 
# Windows users can either launch a new **CMD.exe Prompt** from the **Anaconda Navigator** dashboard and type <code>spyder</code>. Or launch it straight from **Anaconda Navigator** dashboard. Just make sure **Applications on** is set to the **lab1** environment. 
# 
# Those who are familar with <code>spyder</code> can go ahead and copy and paste the code above into the **code editor** and execute it in the **IPython console**. Those who are not familiar can watch [this video](https://www.youtube.com/watch?v=WV9bm4ey7Cg&ab_channel=SpyderIDE) for instructions. 
# 
# Once we have run the code successfully, save this Python script as a <code>.py</code> file in the lab1 folder (i.e. <code>/geospatial-data-science/labs/lab1/</code>).

# ### Make an answers document using Jupyter Notebook
# 
# We will submit the weekly assignments as Jupyter Notebooks (<code>.ipynb</code> format) on GitHub **and** as <code>.pdf</code> documents on Canvas. Keeping the course somewhat connected to Canvas will be useful for organizing and grading. But having a version submitted as a Jupyter Notebook will allow the instructors to test and provide feedback on your code. **Take your time** going through these instructions as the steps outlined here will be the standard way of submitting assignments for the rest of term.
# 
# To make a Jupyter Notebook answers document, type <code>jupyter notebook</code> in the terminal then click **New** from the menu on the upper-right and select **Python 3 (ipykernel)**. Rename this notebook as <code>labX_submission.ipynb</code> where *X* corresponds to the lab number.
# 
# Jupyter Notebooks consist of a linear sequence of cells which include:
# 
# * **Code cells**: for Python code that is run in the kernel
# * **Markdown cells**: for text, images, and equations
# 
# A full guide on how to format these cells can be found [here](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples_index.html).

# ### Task 1 (10 points):
# Edit the short script above slightly and copy and paste it to the new answers notebook. Run the cell one last time to make sure your code has no errors. 
# 
# *********
# 
# ### Task 2 (30 points):
# In the cell below your code, add an image from Google images of somewhere inspiring along with a short caption that includes **bold**, *italics* and a link to the webpage that displays this image. Use the following as a guide: https://www.markdownguide.org/basic-syntax/. Remember the image should be saved in the same folder as your answers notebook (i.e. <code>/geospatial-data-science/labs/lab1/</code>).
# 
# Once you have done this, save and close your answers notebook.
# 
# *********
# 
# ### Task 3 (10 points):
# 
# Send me a direct message on **Slack** with a link to your GitHub profile page. 
# 

# ### Option 1: Submit answers document to GitHub (command line)
# 
# We are now ready to submit our answers document (and our script) via GitHub. To do this in **command line**, we first check to see which files were added/edited.
# 
# <code>git status</code>
# 
# Which should show that there are two new files (one <code>.ipynb</code> file and one <code>.py</code> file). We want to add the notebook to the staging environment which we do using the <code>git add</code> command. 
# 
# <code>git add labX_submission.ipynb</code>
# 
# You can also add the image from Task 2 (e.g. <code>git add image.jpg</code>)
# 
# Now if you rerun the <code>git status</code>, you'll see that git has added both files to the staging environment (notice the "Changes to be committed" line). 
# 
# **NB: only push your answer notebooks (and other relevant files) to your GitHub repository**
# 
# If you make changes to the *assignment notebooks*, command line users can run <code>git checkout filename.ipynb</code> to discard unstaged changes to the file. If the changes were accidently staged, run <code>git reset</code>. 
# 
# Next we will commit these new/edited files by running:
# 
# <code>git commit -m "uploaded first assignment"</code>
# 
# The message at the end of the commit should be something related to what the commit contains - could be a new feature, a bug fix, or just fixing a typo. 
# 
# Finally, we can send these file to our GitHub repository by typing:
# 
# <code>git push</code>
# 
# At this stage, git will probably ask for your username and email which you can configure using:
# 
# <code>git config --global user.name "your name"</code>\
# <code>git config --global user.email "your_email@uoregon.edu"</code>
# 
# In addition, GitHub no longer supports username/password authentication from the command line so users must switch to "personal access tokens" which can be configured using the following instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) or [here](https://swcarpentry.github.io/git-novice/07-github/index.html#ssh-background-and-setup).

# ### Option 2: Submit answers document to GitHub (GitHub Desktop)
# 
# To upload the files to GitHub using **GitHub Desktop**, simply click **Commit to master** in the lower left pane and then **Push to origin**. 
# 
# Again, only push your answers notebooks (and any other new files such as images) to your GitHub repository. If you made changes to the assignment notebooks you can discard these changes by right-clicking on the file in GitHub Desktop and selecting **Discard changes** before clicking **Commit to master**.
# 
# ************
# 
# Both command line and GitHub Desktop users can now go back to their online repository (<code>https://github.com/your_username/geospatial_data_science</code>) to see their first assignment files uploaded. 
# ***********
# 
# Note that we will cover `git` and `GitHub` in more detail in Week 6. If you'd like to learn more about version control in the meantime there are some great online resources:
# * https://swcarpentry.github.io/git-novice/
# * https://www.earthdatascience.org/courses/intro-to-earth-data-science/git-github/
# * https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6 (note that you can read *towardsdatascience.com* without signing up if you open them in incognito mode)

# ### Submit answers document as pdf
# 
# To submit your assignment on Canvas, copy and paste your code (and any written answers to questions) to a **Word Document** and export it as a <code>.pdf</code>. Name this file <code>labX_submission.pdf</code> (where *X* corresponds to the lab number) and submit via Canvas.

# In[ ]:




