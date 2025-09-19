# Wine activity

## Background

In this activity, we will practice some machine learning using the wine dataset. Download the two csv files from [here](https://prodduke-my.sharepoint.com/:f:/g/personal/jr555_duke_edu/Eu8mGsF_wNBGpcAiRJou5pkBtFIvDh5lyecepsdYCeTlrQ?e=TCOkVn). 

```{image} images/wine.png
:width: 500px
:align: center
```

The data provides 13 compostional features for 158 wines grown in the same region in Italy by three different cultivators. The goal is to use these features to determine which of three cultivators the wine belongs to (class 0, 1, or 2).

*****************************

* Activate the `.gds` Python environment by opening an **Anaconda Prompt (miniconda3)** (Windows) or **Terminal** (macOS). Then, on Windows:

```
.gds\Scripts\activate
```

Or, on macOS:

```
source .gds/bin/activate
```

```{note}
Make sure you run this command from the **same directory** as the `.gds` environment folder.
```

* Open a Jupyter Notebook by running:

```
jupyter notebook
```

```{tip}
If you run this command from your course folder, your `.ipynb` assignment will automatically be saved there.
```

*******************

## Task 1 (5 points)

Import the wine features and target labels make a multi-panel figure showing a histogram for each feature (separated by the three wine classes)

Which features are most useful for distinguishing between:

* Class 0 and 1?
* Class 1 and 2?
* Class 0 and 2?

Standardize the features in the dataset and split into training (80%) and testing (20%) datasets. 

* What is the **mean** and **standard deviation** of features in the standardized dataset?

* How many wines are in the training and testing datasets? 

*******************

## Task 2 (5 points)

Train a Decision Tree on the training dataset with a `max_depth=1`. Now use this model to classify wines in the **testing dataset**. 

* What is the mean testing accuracy of this classifier?

Plot a confusion matrix showing the results of the classification for the test dataset.

* Which class has the highest and lowest accuracy?

* For the class with the lowest accuracy, explain why.

*******************

## Task 3 (5 points)

Plot the Decision Tree using the `plot_tree` function which can be imported using:

```
from sklearn.tree import plot_tree
```

* Which feature did the Decision Tree use the split the features?

* What is the **Gini index** of the two groups that are split? Are high values good or bad?

Make a plot showing how testing and training error changes as `max_depth` is increased from 1 to 5.

* At what `max_depth` does training error become 0?

* At what `max_depth` does testing error become 0?

* Which do you think is the **best** model and explain why.

*****************************

```{important}
Save your notebook locally in both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```






