# Assignment 5

## It's competition time!

In this week's lab we will compete to produce the best model for classifying our wine dataset. The data can be downloaded from the [here](https://prodduke-my.sharepoint.com/:f:/g/personal/jr555_duke_edu/Eu8mGsF_wNBGpcAiRJou5pkBtFIvDh5lyecepsdYCeTlrQ?e=Lbv4vU). 

Next Wednesday, we will score models based on their **mean accuracy** on a set of 20 wines that only the instructor as access to. Highest accuracy wins.

```{important}
mean_accuracy = model.score(X, y)
```

```{image} images/wine.png
:width: 500px
:align: center
```

*****************************

## Task 1 (10 points): 

Develop a machine learning model that classifies wine into class 0, 1, or 2 using the dataset available to you. 

To earn full marks on this assignment, we would like to see some evidence of a **systematic search for model performance**. This search could explore different strategies that we have discussed in class including data augmentation, regularization, feature engineering, and/or ensembling. The easiest way to show evidence for these strategies is usually in the form of **learning curves**. Remember, the best performing model will be the one that can **generalize** to new data, not the one that scores 100% on the training data. 

```{hint}
Class 2 is overrepresented in the hidden dataset
```

*****************************


```{important}
Please submit your notebook in `.pdf` format to Canvas by the deadline as evidence of your work.
```