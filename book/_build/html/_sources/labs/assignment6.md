# Assignment 6

In this week's lab we will develop a **neural network** to predict house prices. The data can be downloaded from [here](https://prodduke-my.sharepoint.com/:x:/g/personal/jr555_duke_edu/Efym-RdI_XROu94IYGpwuDcBhB1lLHNjKwh7q-9Pd8LGew?e=eKJUsa) and [here](https://prodduke-my.sharepoint.com/:x:/g/personal/jr555_duke_edu/EY_7YGKJ23RGktDqU6UElFoBlpWkCQFivAI09tbZQ0FUxg?e=ElS3Yj).

```{image} images/houses.png
:width: 500px
:align: center
```

There are two csv files. The first, `house-features.csv`, contains eight attributes for 20640 houses. Note that each row represents some geographic unit (e.g. Census tract) hence columns such as `AveOccup` are decimal numbers. The other file, `house-prices.csv` contains the house prices.

*****************************

## Task 1 (10 points): 

Develop a **multilayer perceptron** that predicts house prices using the features available.

To earn full marks on this assignment, we would like to see some evidence of a **systematic search for model performance**. 

Unlike the previous assignment, this search should focus on the strategies for optimizing the model itself. Things that could be adjusted include:

* Number of hidden layers
* Number of nodes in the hidden layers
* Learning rate
* Regularization (e.g. dropout, L2 penalties)
* Epochs
* Batch size
* Activation functions

Don't attempt to optimize every one of these but please **try at least one**. You can use **learning curves** as evidence for this optimization search. 

```{note}
The best performing model will be the one that can **generalize** to new data, so we will be checking that the dataset was split into training (80%) and testing data (20%) and that the **testing error** was evaluated.
```

*****************************

```{important}
Please submit your notebook in `.pdf` format to Canvas by the deadline as evidence of your work.
```