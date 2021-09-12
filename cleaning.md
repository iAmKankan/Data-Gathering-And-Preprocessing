
### [Missing Value](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/missingvaluehandling.ipynb)
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Ignoring missing values in a data set is a huge mistake as most algorithms simply don’t accept them. 
* Some companies deal with this problem by imputing the missing values based on other observations or dropping the observations with missing values altogether. 
* But these strategies lead to loss of information (note that “no value” also tells us something. 
* If companies miss categorical data, they can label them as “Missing.” Missing numeric data should be flagged and filled with 0 to allow the algorithm estimate the optimal constant for such a situation.
#### The reason of data is missing
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* This part is better be called "data intution", by which it mean "really looking at the  data and trying to figure out why it is the way it is and how that will affect the analysis". 
* For dealing with missing values, you'll need to use your intution to figure out why the value is missing. 
* One of the most important questions you can ask yourself to help figure this out is this:
> **Is this value missing because it wasn't recorded or because it doesn't exist?**

#### Measures for missing data
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* If a value is missing becuase it doesn't exist (like the height of the oldest child of someone who doesn't have any children) then it doesn't make sense to try and guess what it might be. 
* These values you probably do want to keep as _**NaN**_.

* On the other hand, if a value is missing because it wasn't recorded, then you _**can try to guess what it might have been based on the other values in that column and row.**_ 
* This is called **imputation.** 
> _**In statistics, imputation is the process of replacing missing data with substituted values.**_


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


