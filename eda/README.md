## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
#### [_What is Exploratory Data Analysis(EDA) ?_](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/eda/README.md#what-is-exploratory-data-analysiseda-)
* [1. Handling Missing Values](#1-handling-missing-values)
	* [Why does the data get missing?](#why-does-the-data-get-missing)
	* [Measures for missing data](#measures-for-missing-data)
		* [_a. Detecting missing values by using `isna()`, `notna()`_](#a-detecting-missing-values-by-using-isna-notna)
		* [_b. Drop Rows/Columns with "Null" values using `dropna()`_](#b-drop-rowscolumns-with-null-values-using-dropna)
		* [_c.1. Fill NA/missing values using `fillna()`_](#c1-fill-nanan-values-using-fillna)
		* [_c.2. Fill NA/missing values using `interpolate()`_](#c2-fill-namissing-values-using-interpolate)
		* [_c.3. Fill NA/missing values using `replace()`_](#c3-fill-namissing-values-using-replace)
* [2. Data visualization](#2-data-visualization)
* [3. Handling Outliers](#3-handling-outliers)
* [4. Multi Colinearity Detection & Handling](https://github.com/iAmKankan/MachineLearning_With_Python/blob/master/Supervised/Linear%20Regrassion/correlation.md)
#### _Autometic EDA_
* Pandas Profiling
#### [References](#references)
---
## What is Exploratory Data Analysis(EDA) ?
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Exploratory Data Analysis (EDA) is an approach to analyze the data using visual techniques. 
* It is used to discover trends, patterns, or to check assumptions with the help of statistical summary and graphical representations. 
1. Handling Missing Values
2. Data visualization
3. Handling Outliers

### 1. Handling Missing Values
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* It can occur when no information is provided for one or more items or for a whole unit. 
* For Example, Suppose different users being surveyed may choose not to share their income, some users may choose not to share the address in this way many datasets went missing. 
* Missing Data is a very big problem in real-life scenarios. 
* Missing Data can also refer to as NA(Not Available) values in pandas. 
### Why does the data get missing?
* The source of missing data can be very different and here are just a few examples:
  - A value is missing because it was forgotten or lost or not stored properly.
  - For a certain observation, the value of the variable does not exist.
  - The value can't be known or identified.
* One of the most important questions you can ask yourself to help figure this out is this:
> ### **_Is this value missing because it wasn't recorded or because it doesn't exist?_**

### Measures for missing data
* If a value is missing becuase it doesn't exist (like the height of the oldest child of someone who doesn't have any children) then it doesn't make sense to try and guess what it might be. 
* These values you probably do want to keep as _**NaN**_.
* On the other hand, if a value is missing because it wasn't recorded, then _**you can try to guess what it might have been based on the other values in that column and row.**_ 
* This is called **_imputation._** 
> ### _**In statistics, Imputation is the process of replacing missing data with substituted values.**_
* There are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame :
  1. _`isnull()`_
  2. _`notnull()`_
  3. _`dropna()`_
  4. _`fillna()`_
  5. _`replace()`_
  6. _`interpolate()`_
### _Code_
```Python
import numpy as np
import pandas as pd

# passing a dictionary inorder to make a Dataframe
df = pd.DataFrame({'age': [6, 7, np.NaN],
                   'born': [pd.NaT, pd.Timestamp('1998-04-25'),
                            pd.Timestamp('1940-05-27')],
                   'name': ['Alfred', 'Spiderman', ''],
                   'toy': [None, 'Spidertoy', 'Joker']})
df.head()
```
```	
	age	born	      name	toy
0	6.0	NaT	      Alfred	None
1	7.0	1998-04-25   Spiderman Spidertoy
2	NaN	1940-05-27	         Joker
```

### _a. Detecting missing values by using `isna()`, `notna()`_
* The **_isna()_** function is used to detect missing values. Which is the abbriviation of "Is Null"
> _**Series.isna(self)**_
* **Returns: Series- values for each element in Series that indicates whether an element is not an NA value.**

```Python
df.isna()
```
```
age	born	name	toy
0	False	True	False	True
1	False	False	False	False
2	True	False	False	False
```
* **How many missing(NA) values each column has**

```Python3
df.isna().sum()
```
```
age     1
born    1
name    0
toy     1
dtype: int64
```
* **Alternatively, you can call the _`mean()`_ method after _`isnull()`_ to visualise the percentage of the dataset that contains missing values for each variable.**
```Python
df.isnull().mean()
```
```
age     0.333333
born    0.333333
name    0.000000
toy     0.333333
dtype: float64
```
* The **_notna()_** function is used to detect existing (non-missing) values.
> _**Series.notna(self)**_
* **Returns: Series- Mask of bool values for each element in Series that indicates whether an element is not an NA value.**
```Python
# Continuation of above DataFrame
df.isna()
```
```
age	born	name	toy
0	False	True	False	True
1	False	False	False	False
2	True	False	False	False
```

### _b. Drop Rows/Columns with "Null" values using `dropna()`_

* If you're in a hurry or don't have a reason to figure out why your values are missing, one option you have is to just remove any rows or columns that contain missing values. 
> #### Note: Generally this approch is not recommend for important projects! It's usually worth it to take the time to go through your data and really look at all the columns with missing values one-by-one to really get to know your dataset.    
* To drop rows with missing values, Pandas does have a handy function, _**dropna()**_ to help you do this. 
* The **_dropna()_** function is used to return a new Series with missing values removed.
* 
> #### _Series.dropna(self, axis=0, inplace=False, * *kwargs)_
* **Returns: Series- Series with "NA" entries dropped from it.**

#### Row wise drop _NAs_ 
> #### **`axis=0`** default; 0 means 'index' means rows

```Python
df.dropna()
```
```
age	born	name	toy
1	7.0	1998-04-25	Spiderman	Spidertoy
```
#### Column wise drop _NAs_
> #### **`axis=1`**; 1 means 'column' 

```Python
df.dropna(axis=1)
```
```
name
0	Alfred
1	Spiderman
2	
```
* **Note:** A blank space is not considered as 'NaN' or 'None' or 'NA' 


### _c.1. Fill `NA/NaN` values using `fillna()`_
* We can use the Panda's _**fillna()**_ function to fill in missing values in a dataframe.
* One option we have is to specify what we want the "NaN" values to be replaced with. 
* The **`fillna()`** function is used to fill NA/NaN values using the specified method.
> #### _Series.fillna(self, value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, * *kwargs) ;_

* **Returns: Series- Object with missing values filled.**

```Python
df.head()
```
```
	P	Q	R	S
0	NaN	2.0	NaN	0
1	3.0	4.0	NaN	1
2	5.0	NaN	NaN	6
3	NaN	4.0	NaN	5
```
#### Replace all NaN elements with 0s.
```Python
df.fillna(0)
```
```
	P	Q	R	S
0	0.0	2.0	0.0	0
1	3.0	4.0	0.0	1
2	5.0	0.0	0.0	6
3	0.0	4.0	0.0	5
```

#### Only replace maximum number of consecutive `NaN` values to forward/backward fill.
```Python
df.fillna({'P': 0, 'Q': 1, 'R': 2, 'S': 3}, limit=2)
```
```
	P	Q	R	S
0	0.0	2.0	2.0	0
1	3.0	4.0	2.0	1
2	5.0	1.0	NaN	6
3	0.0	4.0	NaN	5
```
#### Propagate non-null values forward or backward.
```Python
# Forward
df.fillna(method='ffill')
```
```
P	Q	R	S
0	NaN	2.0	NaN	0
1	3.0	4.0	NaN	1
2	5.0	4.0	NaN	6
3	5.0	4.0	NaN	5
```

```Python
# Backward
df.fillna(method='bfill')
```
```
	P	Q	R	S
0	3.0	2.0	NaN	0
1	3.0	4.0	NaN	1
2	5.0	4.0	NaN	6
3	NaN	4.0	NaN	5
```

### _c.2. Fill NA/missing values using `interpolate()`_
* The **interpolate()** function is used to interpolate values according to different methods.
> #### _Series.interpolate(self, method='linear', axis=0, limit=None, inplace=False, limit_direction='forward', limit_area=None, downcast=None, * *kwargs) ;_
* **Returns: Series or DataFrame- Returns the same object type as the caller, interpolated at some or all NaN values.**

* **Notes** The ‘krogh’, ‘piecewise_polynomial’, ‘spline’, ‘pchip’ and ‘akima’ methods are wrappers around the respective SciPy implementations of similar names. These use the actual numerical values of the index.

```Python
s.head()
```
```
0    0.0
1    2.0
2    NaN
3    5.0
dtype: float64
```
```Python
s.interpolate()
```
```
0    0.0
1    2.0
2    3.5
3    5.0
dtype: float64
```
#### Filling in NaN in a Series by padding, but filling at most two consecutive NaN at a time.
```Python
df.head()
```
```
0              NaN
1       single_one
2              NaN
3    fill_two_more
4              NaN
5              NaN
6             3.71
7              NaN
```
```Python
s.interpolate(method='pad', limit=2)
```
```
0              NaN
1       single_one
2       single_one
3    fill_two_more
4    fill_two_more
5    fill_two_more
6             3.71
7             3.71
dtype: object
```

### _c.3. Fill NA/missing values using `replace()`_
* Pandas ***dataframe.replace()*** function is used to replace a string, regex, list, dictionary, series, number etc. from a dataframe. 

> #### _DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method=’pad’, axis=None)_
* This is a very rich function as it has many variations.
* The most powerful thing about this function is that it can work with Python regex (regular expressions).

* **Example 1:** Replace team “Boston Celtics” with “Omega Warrior” in the [nba.csv](https://media.geeksforgeeks.org/wp-content/uploads/nba.csv) file
```Python
df[:10]
```

```
	Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	NaN	5000000.0
5	Amir Johnson	Boston Celtics	90.0	PF	29.0	6-9	240.0	NaN	12000000.0
6	Jordan Mickey	Boston Celtics	55.0	PF	21.0	6-8	235.0	LSU	1170960.0
7	Kelly Olynyk	Boston Celtics	41.0	C	25.0	7-0	238.0	Gonzaga	2165160.0
8	Terry Rozier	Boston Celtics	12.0	PG	22.0	6-2	190.0	Louisville	1824360.0
9	Marcus Smart	Boston Celtics	36.0	PG	22.0	6-4	220.0	Oklahoma State	3431040.0
```

* We are going to replace team **“Boston Celtics”** with **“Omega Warrior”** in the **‘df’** data frame
```Python
# this will replace "Boston Celtics" with "Omega Warrior"
df.replace(to_replace ="Boston Celtics", value ="Omega Warrior")
```

```
	Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Omega Warrior	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Omega Warrior	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Omega Warrior	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Omega Warrior	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Omega Warrior	8.0	PF	29.0	6-10	231.0	NaN	5000000.0
...	...	...	...	...	...	...	...	...	...
453	Shelvin Mack	Utah Jazz	8.0	PG	26.0	6-3	203.0	Butler	2433333.0
454	Raul Neto	Utah Jazz	25.0	PG	24.0	6-1	179.0	NaN	900000.0
455	Tibor Pleiss	Utah Jazz	21.0	C	26.0	7-3	256.0	NaN	2900000.0
456	Jeff Withey	Utah Jazz	24.0	C	26.0	7-0	231.0	Kansas	947276.0
457	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
458 rows × 9 columns
```

* **Example 2:** Replacing more than _one value at a time_. Using python list as an argument 
* We are going to replace team **“Boston Celtics”** and **“Texas”** with **“Omega Warrior”** in the **‘df’** dataframe.
```Python
# this will replace "Boston Celtics" and "Texas" with "Omega Warrior"
df.replace(to_replace =["Boston Celtics", "Texas"], 
                            value ="Omega Warrior")
```

```
Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Omega Warrior	0.0	PG	25.0	6-2	180.0	Omega Warrior	7730337.0
1	Jae Crowder	Omega Warrior	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Omega Warrior	30.0	SG	27.0	6-5	205.0	Boston University	NaN
3	R.J. Hunter	Omega Warrior	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Omega Warrior	8.0	PF	29.0	6-10	231.0	NaN	5000000.0
...	...	...	...	...	...	...	...	...	...
453	Shelvin Mack	Utah Jazz	8.0	PG	26.0	6-3	203.0	Butler	2433333.0
454	Raul Neto	Utah Jazz	25.0	PG	24.0	6-1	179.0	NaN	900000.0
455	Tibor Pleiss	Utah Jazz	21.0	C	26.0	7-3	256.0	NaN	2900000.0
456	Jeff Withey	Utah Jazz	24.0	C	26.0	7-0	231.0	Kansas	947276.0
457	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
458 rows × 9 columns
```

* **Example 3**: Replace the Nan value in the data frame with -99999 value.
```Python
# will replace  Nan value in dataframe with value -99999 
df.replace(to_replace = np.nan, value =-99999)
```
```
	Name	Team	Number	Position	Age	Height	Weight	College	Salary
0	Avery Bradley	Boston Celtics	0.0	PG	25.0	6-2	180.0	Texas	7730337.0
1	Jae Crowder	Boston Celtics	99.0	SF	25.0	6-6	235.0	Marquette	6796117.0
2	John Holland	Boston Celtics	30.0	SG	27.0	6-5	205.0	Boston University	-99999.0
3	R.J. Hunter	Boston Celtics	28.0	SG	22.0	6-5	185.0	Georgia State	1148640.0
4	Jonas Jerebko	Boston Celtics	8.0	PF	29.0	6-10	231.0	-99999	5000000.0
...	...	...	...	...	...	...	...	...	...
453	Shelvin Mack	Utah Jazz	8.0	PG	26.0	6-3	203.0	Butler	2433333.0
454	Raul Neto	Utah Jazz	25.0	PG	24.0	6-1	179.0	-99999	900000.0
455	Tibor Pleiss	Utah Jazz	21.0	C	26.0	7-3	256.0	-99999	2900000.0
456	Jeff Withey	Utah Jazz	24.0	C	26.0	7-0	231.0	Kansas	947276.0
457	-99999	-99999	-99999.0	-99999	-99999.0	-99999	-99999.0	-99999	-99999.0
458 rows × 9 columns
```
### 2. Data visualization
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Data Visualization is the process of analyzing data in the form of graphs or maps, making it a lot easier to understand the trends or patterns in the data. 
* There are various types of visualizations – 
   * **Univariate analysis:** This type of data consists of only one variable. The analysis of univariate data is thus the simplest form of analysis since the information deals with only one quantity that changes. It does not deal with causes or relationships and the main purpose of the analysis is to describe the data and find patterns that exist within it.
   * **Bi-Variate analysis:** This type of data involves two different variables. The analysis of this type of data deals with causes and relationships and the analysis is done to find out the relationship among the two variables.
   * **Multi-Variate analysis:** When the data involves three or more variables, it is categorized under multivariate.

### 3. Handling Outliers
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* **_Outliers_** are data values that are far outside the rest of the observations in your dataset. 
* Depending on the context, you sometimes might hear outliers referred to as **_anomalies_**.
* For example, if the age of most college going students in a dataset is between 18 and 25, an observation of 60 for the age of a student would be considered an outlier
* Generally, Outliers affect statistical results while doing the EDA process, we could say a quick example is the **MEAN** and **MODE** of a given set of data set, which will be misleading that the data values would be higher than they really are.
* The **CORRELATION COEFFICIENT** is highly sensitive to outliers. 
	* Since it measures the strength of a linear relationship between two variables and the relationship dependent of the data. 
	* correlation is a non-resistant measure and r (**correlation coefficient**) is strongly affected by outliers.
		* **Positive Relationship** When the correlation coefficient is closer to value 1
		* **Negative Relationship** When the correlation coefficient is closer to value -1
		* **Independent** When X and Y are independent, then the correlation coefficient is close to zero (0) 

### Are Outliers always bad?
* Outliers in some cases can be useful for detection of abnormal activities. 
	* For instance, if a person accesses her online bank account from a specific location 95% of the time and then suddenly her bank account is accessed from a geographical location far from her previous login, the new login will be treated as an outlier and can be helpful in fraud detection.
* Outliers can also occur in your dataset due to human mistakes while entering data or even a failure of a data recording device. 
 	* In such cases, outliers can distort the distribution of data and convey erroneous information. If not handled, this can affect the performance of statistical algorithms like machine learning models.

### Should I drop Outliers?
* Before dropping the Outliers, we must analyze the dataset with and without outliers and understand better the impact of the results.
* If you observed that it is obvious due to incorrectly entered or measured, certainly you can drop the outlier. No issues on that case.
* If you find that your assumptions are getting affected, you may drop the outlier straight away, provided that no changes in the results.
* If the outlier affects your assumptions and results. No questions simply drop the outlier and proceed with your further steps.


## References:
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [Geeks For Geeks](https://www.geeksforgeeks.org/what-is-exploratory-data-analysis/)
* [Wellsr.com](https://wellsr.com/python/outlier-data-handling-with-python/)
