# Assignment 6

```{admonition} Deadline
Please complete this assignment before **Feb 24, 11:59pm**.
```

*****************************

## Task 1 (40 points)

Prepare a `README.md` file in your new repo that will serve as the landing page for your project. You can continue to update it as your project evolves, but for now, please prepare a basic project outline.  

Review the [markdown cheat sheet](https://www.markdownguide.org/basic-syntax/) and use some basic headings, bulleted/numbered lists, and other formatting to organize your outline. We recommend using a **markdown editor** such as [MacDown](https://macdown.uranusjr.com/) for MacOS or [Ghostwriter](https://wereturtle.github.io/ghostwriter/download.html) for Windows.

Please include the following in `README.md`:

* Project Title
* Name(s) of individual or team members
* Short 1-2 sentence summary
* Problem statement, question(s) and/or objective(s)
* Datasets you will use (with links, if available)
* Python packages that team members require
* Planned methods/approach
* Expected outcomes
* Any other relevant information, images/tables, references, etc.
* References

That may sound like a lot, but some of these items should only be 1-2 sentences, others can be short lists. Consider this the start of your final report. 

We would like to see at **least one commit** from **each group member** at this phase of the project, even if it is as simple as adding their name to the `README.md` file. 

*****************************

## Task 2 (10 points)

Push all changes to GitHub and submit README as a pdf to Canvas. The markdown editors should be able to export `.md` files as `.pdf`

*****************************

## Some notes for final projects

* Start early! 

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

* Commit **early**, commit **often**


```{important}
Save your README locally as both `.md` and `.pdf` formats but only submit the **pdf** to Canvas.
```