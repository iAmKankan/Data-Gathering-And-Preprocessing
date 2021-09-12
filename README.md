## Preprocessing:
 ![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

 ![preprocessing](https://user-images.githubusercontent.com/12748752/126914717-48cc96d8-956a-4e6d-88b6-0166fb71290e.jpg)
 ### Data Cleaning
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
 #### The reason of data is missing
* This part is better be called "data intution", by which it mean "really looking at the  data and trying to figure out why it is the way it is and how that will affect the analysis". 
* For dealing with missing values, you'll need to use your intution to figure out why the value is missing. 
* One of the most important questions you can ask yourself to help figure this out is this:
> **Is this value missing because it wasn't recorded or because it doesn't exist?**

* If a value is missing becuase it doesn't exist (like the height of the oldest child of someone who doesn't have any children) then it doesn't make sense to try and guess what it might be. 
 * These values you probably do want to keep as _**NaN**_.
* On the other hand, if a value is missing because it wasn't recorded, then you _**can try to guess what it might have been based on the other values in that column and row.**_ 
* This is called **imputation.** 
> _**In statistics, imputation is the process of replacing missing data with substituted values.**_




 ### [Data transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/datatransformation.md)
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* [Feature Scaling](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/datatransformation.md#feature-scaling)
  * [Normalization And Standardization](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
  * [Scaling to Minimum And Maximum values](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
  * [Scaling To Median And Quantiles](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
* [Gaussian Distribution](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
  * [Logarithmic Transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
  * [Reciprocal Trnasformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
  * [Square Root Transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
  * [Exponential Trnasformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
  * [Box Cox Transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 

 ### Data Reduction
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

 
 
 
 
 ![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

 
#### List of Machine Learning algorithms which are sensitive to outliers:
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

1. Linear Regression
2. Logistic Regression
3. Support Vector Machine
4. K- Nearest Neighbors
5. K-Means Clustering
6. Hierarchical Clustering
7. Principal Component Analysis

#### List of Machine Learning algorithms which are not sensitive to outliers:
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

1. Decision Tree
2. Random Forest
3. XGBoost
4. AdaBoost
5. Naive Bayes

 
