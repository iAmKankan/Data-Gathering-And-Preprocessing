![preprocessing](https://user-images.githubusercontent.com/12748752/126914717-48cc96d8-956a-4e6d-88b6-0166fb71290e.jpg)

## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [Bias and Varience](https://github.com/iAmKankan/MachineLearning_With_Python#bias-and-varience)
* [Overfitting and Underfitting](https://github.com/iAmKankan/MachineLearning_With_Python#overfitting-and-underfitting)
* [**Data Cleaning**](#data-cleaning)
  * [**Missing Value**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#missing-value)
    * [Identify missing value.](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#the-reason-of-data-is-missing)
    * [Dorping missing value.](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#drop-missing-values)
    * [Auto filling missing value](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/cleaning.md#filling-in-missing-values-automatically)
  * [**Parsing Dates**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/date_parsing.md)
  * [**Character encoading**]()
  * [Multi Colinearity](https://github.com/iAmKankan/MachineLearning_With_Python/blob/master/Supervised/Linear%20Regrassion/correlation.md)
* [**Data transformation**](#data-transformation)
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
* [**Feature Selection**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/tree/main/feature_selection#readme)
* [**Data Reduction**](#data-reduction)
  * [Dimentionlity Reduction](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/tree/main/Dimensionality_Reduction)




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



### Data Reduction
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
### Curse of Dimentionlity
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* The curse of dimensionality basically means that the error increases with the increase in the number of features. 
* It refers to the fact that algorithms are harder to design in high dimensions and often have a running time exponential in the dimensions.
*  A higher number of dimensions theoretically allow more information to be stored, but practically it rarely helps due to the higher possibility of noise and redundancy in the real-world data.
 
 * **In machine learning,** a small increase in the dimensionality would require a large increase in the volume of the data in order to maintain a similar level of performance.
 * Thus the curse of dimensionality is the expression of all phenomena that appear with high-dimensional data, and that have most often unfortunate consequences on the behavior and performances of learning algorithms.
 
 #### How to combat CoD
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
 * **Dimensionality Reduction**
 * **Regularisation**
 * **Principal Component Analysis(PCA)**


#### Where to use
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* It Works on Statistical Concept based Machine Learning Algorithms
  * Random forest doesnot need Dimensionality Reduction
  * Although Neural Net doesnot works very good but doesnot need Dimensionality Reduction.
 
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
