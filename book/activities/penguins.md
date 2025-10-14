# Penguin activity

## Background

In this activity, we will install `TensorFlow` and use it to make a neural network for predicting Penguin species from the Palmer Penguin dataset. The data can be downloaded from [here](https://prodduke-my.sharepoint.com/:x:/g/personal/jr555_duke_edu/EaznIuIOlXxJkj0plnFf8wwBAH39AMJryACM-WzQe-UijQ?e=lc9Pzi). 

```{image} images/penguins.png
:width: 600px
:align: center
```
Artwork by @allison_horst

We talked about it in class but, as a reminder, this dataset contains attributes for 342 penguins collected from three islands in the Palmer Archipelago, Antarctica. More information about the Palmer Penguin dataset can be found [here](https://allisonhorst.github.io/palmerpenguins/index.html). 

Our goal in this activity is to predict body mass using the other features in the dataset (i.e. culmen length, culmen depth, and flipper length). To do this, we will perform **regression** using a neural network.

*****************************

## Task 1 (0 points)

We first need to install `TensorFlow` which, on MacOS at least, requires Python 3.9-3.11. The easiest way to do this is to open an **Anaconda Prompt (miniconda3)** (Windows) or **Terminal** (macOS) and create a new environment called `tf`:

```
conda create --name tf python=3.11
```

Activate the environment:

```
conda activate tf
```

* Install `tensorflow` using `pip`:

```
pip install tensorflow
```

* Install some other packages:

```
pip install notebook pandas matplotlib scikit-learn
```

* Open a `jupyter notebook`

```
jupyter notebook
```

```{tip}
If you run this command from your course folder, your `.ipynb` assignment will automatically be saved there.
```

*******************

## Task 2 (0 points)

Import the Penguin dataset by running the following:

```{note}
You will need to change the path name to the csv file
```

```
# Import packages
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Read training data
df = pd.read_csv(`data/penguins.csv')

# Define feature list
feature_list =  ['Culmen Length (mm)', 'Culmen Depth (mm)',
       'Flipper Length (mm)']
X = df[feature_list]
y = df['Body Mass (g)']

# Standarize features
x_scaler = StandardScaler()  
X_scaled = x_scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)
X_scaled.index = X.index

y_scaler = StandardScaler()  
y_scaled = y_scaler.fit_transform(y.values.reshape(-1, 1))
y_scaled = pd.DataFrame(y_scaled.flatten(), index=y.index, columns=[y.name])

# Split into training, testing, and validation
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=42)
```

To expedite things, this code standardizes the data and defines training and testing datasets. 

*******************

## Task 3 (10 points)

* Build a feedforward neural network that predicts `y_train` from `X_train` using `TensorFlow`. 


```{note}
The model should contain at least one hidden layer. 
```

* Evaluate the **mean absolute error** (MAE) of your model by running:

```
# Predict on test set
y_pred_scaled = model.predict(X_test).flatten()
y_pred = y_scaler.inverse_transform(y_pred_scaled.reshape(1, -1)).flatten()
y_actual = np.array(y_scaler.inverse_transform(y_test)).flatten()

# Report MAE
print('MAE = %.2f g' % (np.mean(np.abs(y_actual-y_pred))))
```

* Plot the predictions of your model by running:

```
# Plot
fig, ax = plt.subplots(figsize=(10, 4))
ax.scatter(y_actual, y_pred, zorder=3)
ax.plot([2500, 6500], [2500, 6500], lw=2, zorder=3)
ax.set_ylabel('Predicted body mass (g)', fontsize=12)
ax.set_xlabel('Actual body mass (g)', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.grid(ls='dashed', lw=1, zorder=1)
ax.text(0.05, 0.95, f"MAE = {mae:.2f} g", transform=ax.transAxes, 
        fontsize=12, verticalalignment='top', 
        bbox=dict(boxstyle="round,pad=0.3", fc="white", 
              ec="black", alpha=0.7))
```

*******************

## Task 3 (5 points)

Tinker with your model to see if you can improve your MAE. 

```{note}
Students who can reduce their MAE to < 275 g will receive a bonus point.
``` 

*****************************

```{important}
Save your notebook locally in both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```






