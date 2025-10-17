# Contributing to a GitHub repository

In this activity we will learn how to contribute to an existing project to which we don't have **push access**. To do this, will "fork" the course website, edit one of the files, push changes to GitHub, and open a **pull request**. 

```{note}
In this workflow, projects don't have to worry about adding users as collaborators to give them push access.
```

*****************************

## Fork, clone, and branch

* To begin this activity, go to the [course website](https://github.com/ryan-lab-duke/gds-applications-site) and click the **Fork** button in the top right. Leave everything as is on the next page and click **Create fork**. When we do this, GitHub will make a copy of the project that lives in our namespace that we can push to. 

* **Clone** this new remote repository locally by running:

```bash
git clone git@github.com:<username>/gds-applications-site.git
```

```{note}
Where `<username>` is your GitHub username.
```

* Create a new branch by running:

```bash
git checkout -b suggested_edit
```

*****************************

## Make a change

Make a change on the course website. Don't worry, you can't break anything.

* At the very least, add your name to the `add-name.md` file in `book/activities/contribution/`(I will delete this file at the end of the activity).

* But, if you can find a spelling or grammatical error, I would be very appreciative - I know there are many! 

* Alternatively, you could make a comment about a part of a lecture/activity/assignment you liked or disliked.

*****************************

## Commit and push

Once you have made your changes, **commit** your changes and **push** your branch to your remote repository.

```bash
git commit -a -m "edit"
git push --set-upstream origin suggested_edit
```

*****************************

## Submit a pull request

* Go to your repository in GitHub.com and click **Compare & pull request**.

* **Title** your pull request and add a **description**. It is almost always worthwhile to put some effort into this, since a good description helps the owner of the original project determine what you were trying to do.

* Click **Create pull request**

That's it, we have submitted our first pull request. I will now review your changes and decide whether to accept them or not. 

* Now we can clean up by running:

```bash
git checkout main
git branch -d suggested_edit
```

*****************************

## Receive a pull request

We have provided some edits on your `README.md` in your final project repository and submitted a pull request. Now it is your turn to incorporate our pull request. 

* Click **pull requests** from the top menu of your final project repository and then on the pull request that was opened by **JohnnyRyan1**

* Review the pull request by clicking on **Commits** and add a comment (without approving)

* Let's assume that my edits were useful (you can delete them later). Click **Merge pull request** and **Confirm merge**.

* Download the changes locally by running:

```bash
git pull
```

* Confirm that the changes we made have been incorporated into the `README.md` file. 

*****************************

```{important}
Take a screenshot to confirm that my pull request has been successfully closed and submit as a **pdf** to Canvas.
```





  

