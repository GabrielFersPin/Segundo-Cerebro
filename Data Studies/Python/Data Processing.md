
#DataAnalysis #Python #SQL 


- Diabetes dataset in csv

### About this dataset[[Python Links]]

- Context: originally from the **National Institute of Diabetes and Digestive and Kidney Diseases.** The objective of the dataset is to diagnostically predict wheter or not a patient has diabetes, based on certain diagnostic measurements included in the dataset.
- Content: The dataset consists of several medical predictor variables and one target variable, Outcome.

```python
# Import pandas library
import pandas as pd
```

```python
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "diabetes.csv")
df = pd.read_csv("diabetes.csv")
```

After reading the dataset we can use the dataframe.head(n) method to check the top n rows of the data frame 

```python
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
```

To view the dimension of the dataframe

```python
df.shape

```

### Statistical Overview of the dataset

```python
df.info()
```

```python
df.describe()
```

### Identify and handle missing values

.isnull()

.isnotnull()

The output is a boolean value indicating wheter the value that is passed into the argument is in fact missing data

```python
missing_data = df.isnull()
missing_data.head()
```

### Count missing values in each column

```python
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
```

### Correct data format

**.dtype()** to check if the data type

**.astype()** to change the data type 

```python
df.dtypes
```

### Visualization

Seaborn and Matplotlib is the most powerfull tools for visualize the data and get insights

```python
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns
```