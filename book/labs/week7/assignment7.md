# Assignment 8

In this activity, we will develop a convolutional network to perform image classification on the EuroSAT dataset which can be accessed [here](https://zenodo.org/records/7711810). We will just be using the RGB version so download the `EuroSAT_RGB.zip` file. 

As a reminder, this dataset contains 27,000 labeled Sentinel-2 images over Europe with ten different land use and land cover classes. 

*****************************

## Task 1 (10 points): 

Develop a convolutional network to classify the EuroSAT dataset. 

To earn full marks on this assignment, we would like to see some evidence of tinkering to improve model performance. 

Since training on this dataset takes a long time, you probably won't be able to carry out an extensive hyperparameter optimization search. Therefore you probably will not be able to produce learning curves.

That said, we'd like to see some effort to optimize the model. Please don't submit the same model that was used in the class activity. Things that could be adjusted include:

* Number of hidden layers
* Number of nodes in the hidden layers
* Learning rate
* Regularization (e.g. dropout, L2 penalties)
* Epochs
* Batch size
* Activation functions

## Task 2 (10 points)

Evaluate the model using a confusion matrix to answer the following questions:

a) Which classes have the highest and lowest overall **mean accuracy**?

b) Which classes have the highest and lowest **precision**?

c) Which classes have the highest and lowest **recall**?

*****************************

```{important}
Save your notebook locally in both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```






