## Preprocessing:
 ![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

 ![preprocessing](https://user-images.githubusercontent.com/12748752/126914717-48cc96d8-956a-4e6d-88b6-0166fb71290e.jpg)
 ### [Data Cleaning](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md)
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* [**Missing Value**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#missing-value)
  * [Identify missing value.](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#the-reason-of-data-is-missing)
  * [Dorping missing value.](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#drop-missing-values)
  * [Auto filling missing value](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#filling-in-missing-values-automatically)




 ### [Data transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/datatransformation.md)
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Feature transformation is simply a function that transforms features from one representation to another. 
* But why would we transform our features? Well there are many reasons, such as:
  *  Data types are not suitable to be fed into a machine learning algorithm, e.g. text, categories
  *  Feature values may cause problems during the learning process, e.g. data represented in different scales
  *  We want to reduce the number of features to plot and visualize data, speed up training or improve the accuracy of a specific model
  *  Linear Regression uses Gradient Descent for its calculation of Global Minima thats needs a even scaled data for better a prediction.
  *  Algorithms like KNN,K Means,Hierarichal Clustering use Eucledian Distance, Manhattan Distance etc. for the peorpose of mesure the distance between observations, They need scaled data too for the better a prediction.
  *  Deep Learning Techniques needs Standardization, Scaling they are also Feature Transformation techniques.

### Types Of Transformation 
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

 
