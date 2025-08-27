# Activity 1

Download the data for the assignment from [here](https://www.dropbox.com/scl/fi/zcqevrwv51k3oahjwwz7k/rivers.csv?rlkey=aal2mmo2kk6exeor3mw9i4lir&dl=0). This dataset contains attributes for the some of the largest rivers in the world. In this activity, we will use the `pandas` package to do some basic analysis on this dataset. 

```{image} images/global-rivers.webp
:width: 600px
:align: center
```
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

```{note}
If you run this command from your course folder, your `.ipynb` assignment will automatically be saved there.
```

*****************************

## Task 1 (5 points)

* Import the `pandas` package (i.e. `import pandas as pd`) and read the data (i.e. `pd.read_csv`)

Write some code that prints the following information:

* Number of columns

* Number of rows

* The maximum `Average discharge (m3/s)` value

* The minimum `Drainage area (km2)` value

* The mean `Length (km)` value

*****************************

## Task 2 (5 points)

Answer the following questions:

* What is the name of the shortest river?

* How many of these rivers are located in North America?

* What is the mean and standard deviation of `Average discharge (m3/s)` (of entire DataFrame)?

* What are the names of the rivers that flow into the Atlantic Ocean?

* Which continent contains the most large rivers?

*****************************

## Task 3 (5 points)

* Add a column called `Primary` that has value of `1` if the river `Type` is `Primary River` and `0` if the river is a `Tributary River`. 

* Make a new DataFrame of just the `Primary` rivers.

* Write a `for` loop that prints the name of each river in this new DataFrame.

* Write another `for` loop that only prints the name of the river if it starts with the letter `M`.

* Modify the `for` loop so it saves the names of these rivers as a `list`. 


```{important}
Save your notebook locally in both `.ipynb` and `.pdf` formats but only submit the **pdf** to Canvas.
```

