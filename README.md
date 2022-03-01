## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
### [EDA (_Exploratory Data Analysis_) and Preprocessing](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/tree/main/eda)
   * [**Missing Value Detection & Handling**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#missing-value)
     * [Identify missing value.](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#the-reason-of-data-is-missing)
     * [Dorping missing value.](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#drop-missing-values)
     * [Auto filling missing value](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#filling-in-missing-values-automatically)
   * [**Data visualization**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/eda/README.md#2-data-visualization)
   * [**Outliers Detection & Handling**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/eda/README.md#3-handling-outliers)
   * [**Multi Colinearity Detection & Handling**](https://github.com/iAmKankan/MachineLearning_With_Python/blob/master/Supervised/Linear%20Regrassion/correlation.md)
### _Data Preprocessing_
  * [**Data Cleaning**](#data-cleaning)
  * [**Data transformation**](#data-transformation)
    * [Feature Scaling](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/datatransformation.md#feature-scaling)
      1. [Normalization And Standardization](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
      1. [Scaling to Minimum And Maximum values](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
      1. [Scaling To Median And Quantiles](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/scaling.ipynb)
    * [Gaussian Distribution](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
      1. [Logarithmic Transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
      1. [Reciprocal Trnasformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
      1. [Square Root Transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
      1. [Exponential Trnasformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
    * [Box Cox Transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/gaussian.ipynb) 
* [**Parsing Dates**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/date_parsing.md)
* [**Character Encoading**]()
* [**Categorical Encoading**]()
* [**Feature Selection**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/tree/main/feature_selection#readme)
* [**Handling Imbalanced Data**]()
* [**Data Reduction**](#data-reduction)
  * [Dimentionlity Reduction](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/tree/main/Dimensionality_Reduction)
### [_**Model Deployment**_](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/README.md)
### _Common Terms_
   * [Bias and Varience](https://github.com/iAmKankan/MachineLearning_With_Python#bias-and-varience)
   * [Overfitting and Underfitting](https://github.com/iAmKankan/MachineLearning_With_Python#overfitting-and-underfitting)

## Variables
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
![variables2](https://user-images.githubusercontent.com/12748752/156125379-013f22a6-ff21-4986-84fb-e22cd434509d.png)

### [Data Cleaning](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md)
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Datasets usually contain large volumes of data that may be stored in formats that are not easy to use. 
* That’s why data scientists need first to make sure that data is correctly formatted and conforms to the set of rules.
*  Data sparseness and formatting inconsistencies are the biggest challenges – and that’s what data cleansing is all about. 
>  Data cleaning is a task that identifies incorrect, incomplete, inaccurate, or irrelevant data, fixes the problems, and makes sure that all such issues will be fixed automatically in the future.
*  According to Appen, data scientists spend 60% of the time organizing and cleansing data!

 ### [Data transformation](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/datatransformation.md)
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Feature transformation is simply a function that transforms features from one representation to another. 
* But why would we transform our features? Well there are many reasons, such as:
  *  Data types are not suitable to be fed into a machine learning algorithm, e.g. text, categories
  *  Feature values may cause problems during the learning process, e.g. data represented in different scales
  *  We want to reduce the number of features to plot and visualize data, speed up training or improve the accuracy of a specific model
  *  Linear Regression uses Gradient Descent for its calculation of Global Minima thats needs a even scaled data for better a prediction.
  *  Algorithms like KNN,K Means,Hierarichal Clustering use Eucledian Distance, Manhattan Distance etc. for the peorpose of mesure the distance between observations, They need scaled data too for the better a prediction.
  *  Deep Learning Techniques needs Standardization, Scaling they are also Feature Transformation techniques.





 
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
