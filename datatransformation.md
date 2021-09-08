 
### Feature Transformation
 ![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

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

1. [Normalization And Standardization](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
2. [Scaling to Minimum And Maximum values](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
3. [Scaling To Median And Quantiles](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
4. Guassian Transformation
5. Logarithmic Transformation
6. Reciprocal Trnasformation
7. Square Root Transformation
8. Exponential Trnasformation
9. Box Cox Transformation


##  [Feature Scaling](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
 ![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

* In practice, different types of variables are often encountered in the same data set. A significant issue is that the range of the variables may differ a lot. Using the original scale may put more weight on the variables with a large range. In order to deal with this problem, the technique of features rescaling need to be applied to independent variables or features of data in the step of data preprocessing.
* The terms "normalization" and "standardization" are sometimes used interchangeably, but they usually refer to different things.


* The goal of applying feature scaling is to make sure features are on almost the same scale so that each feature is equally important and make it easier to process by most machine-learning algorithms
###  Where does Feature Scaling is needed?
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* Some machine learning models are fundamentally based on distance matrix, also known as the distance-based classifier, for example, K-Nearest-Neighbours, SVM, and Neural Network. * Feature scaling is extremely essential to those models, especially when the range of the features is very different. Otherwise, features with a large range will have a large influence in computing the distance.

### [Standardisation vs Max-Min Normalization](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Standardisation is more robust to outliers, and in many cases, it is preferable over Max-Min Normalisation.
* In contrast to standardisation, we will obtain smaller standard deviations through the process of Max-Min Normalisation.
* Max-Min Normalisation typically allows us to transform the data with varying scales so that no specific dimension will dominate the statistics, and it does not require making a very strong assumption about the distribution of the data, such as k-nearest neighbours and artificial neural networks.
*  However, Normalisation does not treat outliners very well.
*  On the contrary, standardisation allows users to better handle the outliers and facilitate convergence for some computational algorithms like gradient descent. Therefore, we usually prefer standardisation over Min-Max Normalisation.

### Note:
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* If an algorithm is not distance-based, feature scaling is unimportant, including Naive Bayes, Linear Discriminant Analysis, and Tree-Based models (gradient boosting, random forest, etc.).

![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

## Gaussian Distribution
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

* In Machine learning or Deep Learning, some of the models such as Linear Regression, Logistic Regression, Artificial Neural Networks assume that features are normally distributed and can perform much better if the features provided to them during modeling are normally distributed.

* A normal distribution is sometimes informally called a bell curve.
* Samples of the Gaussian Distribution follow a bell-shaped curve and lies around the mean. The mean, median, and mode of Gaussian Distribution are the same.

* In probability theory, a normal (or Gaussian) distribution is a type of continuous probability distribution for a real-valued random variable. 

 ![image](https://user-images.githubusercontent.com/12748752/132567846-965a6592-ed4b-4458-baa4-3baefb0cf88f.png)

### Various Transformations to change the distribution of features
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* Log Transformation
* Square root Transformation
* Reciprocal Transformation
* Exponential Transformation
* Box-Cox Transformation

### How to check if a variable is following Normal Distribution?
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Histogram
* Q-Q plot
* KDE plot
* Skewness and Kurtosis
* Five Number Summary 
