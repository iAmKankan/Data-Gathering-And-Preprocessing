## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

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
### Why is data missing?
* The source of missing data can be very different and here are just a few examples:
  - A value is missing because it was forgotten or lost or not stored properly.
  - For a certain observation, the value of the variable does not exist.
  - The value can't be known or identified.
* One of the most important questions you can ask yourself to help figure this out is this:
> #### **_Is this value missing because it wasn't recorded or because it doesn't exist?_**

### Measures for missing data
* If a value is missing becuase it doesn't exist (like the height of the oldest child of someone who doesn't have any children) then it doesn't make sense to try and guess what it might be. 
* These values you probably do want to keep as _**NaN**_.
* On the other hand, if a value is missing because it wasn't recorded, then you _**can try to guess what it might have been based on the other values in that column and row.**_ 
* This is called **imputation.** 
> #### _**In statistics, imputation is the process of replacing missing data with substituted values.**_


#### [Drop missing values](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/missingvaluehandling.ipynb)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* If you're in a hurry or don't have a reason to figure out why your values are missing, one option you have is to just remove any rows or columns that contain missing values. 

> Note: Generally this approch is not recommend for important projects! It's usually worth it to take the time to go through your data and really look at all the columns with missing values one-by-one to really get to know your dataset.    

* To drop rows with missing values, Pandas does have a handy function, _**dropna()**_ to help you do this. 

#### [Filling in missing values automatically](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/missingvaluehandling.ipynb)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* We can use the Panda's _**fillna()**_ function to fill in missing values in a dataframe for us.
* One option we have is to specify what we want the NaN values to be replaced with. 
* Here, I would like to replace all the NaN values with 0.

> _df.fillna({'NameColumn':8,'AddressColumn':0})_ 

> _df[['col1', 'col2']].fillna(value=0, inplace=True)_



* There are several useful functions for detecting, removing, and replacing null values in Pandas DataFrame :
  1. isnull()
  2. notnull()
  3. dropna()
  4. fillna()
  5. replace()
  6. interpolate()
* [Jupyter Notebook for the above Pandas function](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/missingvaluehandling.ipynb)
### 2. Data visualization
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Data Visualization is the process of analyzing data in the form of graphs or maps, making it a lot easier to understand the trends or patterns in the data. 
* There are various types of visualizations – 
   * **Univariate analysis:** This type of data consists of only one variable. The analysis of univariate data is thus the simplest form of analysis since the information deals with only one quantity that changes. It does not deal with causes or relationships and the main purpose of the analysis is to describe the data and find patterns that exist within it.
   * **Bi-Variate analysis:** This type of data involves two different variables. The analysis of this type of data deals with causes and relationships and the analysis is done to find out the relationship among the two variables.
   * **Multi-Variate analysis:** When the data involves three or more variables, it is categorized under multivariate.

### 3. Handling Outliers
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* An Outlier is a data-item/object that deviates significantly from the rest of the (so-called normal)objects. 
* They can be caused by measurement or execution errors. 
* The analysis for outlier detection is referred to as outlier mining. 
* There are many ways to detect the outliers, and the removal process is the data frame same as removing a data item from the panda’s dataframe.

### Removing Outliers
* For removing the outlier, one must follow the same process of removing an entry from the dataset using its exact position in the dataset because in all the above methods of detecting the outliers end result is the list of all those data items that satisfy the outlier definition according to the method used.



## References:
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [Geeks For Geeks](https://www.geeksforgeeks.org/what-is-exploratory-data-analysis/)
