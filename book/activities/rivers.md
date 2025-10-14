# Rivers of the World Activity

In this activity, we will practice working with table data in Python. Download the data for the assignment from [here](https://prodduke-my.sharepoint.com/:x:/g/personal/jr555_duke_edu/ETFKJhCx9a5LrWvxNhFSvDIB3RAJT9G2zCHt_rsCedRZCg?e=uBa4oL). This dataset contains attributes for the some of the largest rivers in the world. In this activity, we will use the `pandas` package to do some basic analysis on this dataset. 

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

* Number of rows and columns

* The maximum `Average discharge (m3/s)` value

* The minimum `Drainage area (km2)` value

* The mean `Length (km)` value

* What is the name of the shortest river?

* Compute the ratio of discharge to drainage area (m³/s per km²) for each river. Which river is most "efficient" at draining water relative to its basin size?

********************************

```{important}
We recommend presenting your **numerical answers** in a readable way using string formatting. See [this guide](https://ryan-lab-duke.github.io/gds-applications-site/course-info/format.html) for more info.
```

## Task 2 (5 points)

Answer the following questions:

* How many of these rivers are located in North America?

* What are the names of the rivers that flow into the Atlantic Ocean?

* Which continent contains the most rivers?

* Which continent has the longest rivers (on average)?

*  If the Mississippi and Missouri were combined into a single river, what would their combined discharge, length, and drainage area be? How would it rank globally?

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

