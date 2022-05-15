## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [The Curse of Dimensionality](#the-curse-of-dimensionality)
* [What is Dimensionality Reduction?](#what-is-dimensionality-reduction)
* [Dimensionality Reduction benefits](#dimensionality-reduction-benefits)
   1. [Feature selection](#1-feature-selection)
   2. [Feature extraction](#2-feature-extraction)
 * [Principal Component Analysis(PCA)](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Dimensionality_Reduction/PCA.md)

### The Curse of Dimensionality
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
> **_The curse of dimensionality_** is a problem that arises when we are working with a _lot of data having multiple features_ or we can say it as _**high dimensional data**_. 

The curse of dimensionality is the expression of all phenomena that appear with **high-dimensional** data, and that have most often unfortunate consequences on the behavior and performances of learning algorithms.

### ◼️ _Dimension_
The dimension of the data means the number of features or columns in our dataset. 

### ◼️ _The Problem_
**In machine learning,** a small increase in the dimensionality would require a large increase in the volume of the data in order to maintain a similar level of performance.

### Issue 01 : _Increase in computation time_:-
Majority of the **machine learning algorithms** they rely on the **calculation of distance** for _model building_ and as the number of dimensions increases it becomes more and more **computation-intensive** to create a model out of it. 

**_For one dimension_ 1D:** if we have to calculate the distance between two points in just one dimension, like two points on the number line, we’ll just subtract the coordinate of one point from another and then take the magnitude:
##### the formula is-  <img src="https://latex.codecogs.com/svg.image?\large&space;\mathbf{{\color{Purple}(x_1-x_2)}&space;}" title="https://latex.codecogs.com/svg.image?\large \mathbf{{\color{Purple}(x_1-x_2)} }" align="center"/>

**_For Two dimension_ 2D:** if we need to calculate the distance between two points in two dimensions.
##### the formula is- <img src="https://latex.codecogs.com/svg.image?\large&space;\mathbf{{\color{Purple}\sqrt{(x_1-x_2)^2&plus;(y_1-y_2)^2}}&space;}" title="https://latex.codecogs.com/svg.image?\large \mathbf{{\color{Purple}\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}} }" align="center" />

**_For Three dimension_ nD:** if we need to calculate the distance between two points in three dimensions
##### the formula is- <img src="https://latex.codecogs.com/svg.image?\large&space;\mathbf{{\color{Purple}\sqrt{(x_1-x_2)^2&plus;(y_1-y_2)^2&space;&plus;&space;(z_1-z_2)^2&plus;&space;\cdots&plus;(n_1-n_2)^2}}&space;}" title="https://latex.codecogs.com/svg.image?\large \mathbf{{\color{Purple}\sqrt{(x_1-x_2)^2+(y_1-y_2)^2 + (z_1-z_2)^2+ \cdots+(n_1-n_2)^2}} }" align="center"/>

This is the effort of calculating the distance between two points. Just imagine the number of calculations involved for all the data points involved.

One more point to consider is that as the number of dimension increases, points are going far away from each other. This means that any new point that comes when we are testing the model is going to be farther away from our training points. This leads to a less reliable model, and it makes our model overfitted to the training data.


* **Hard (or almost impossible) to visualise the relationship between features:** As stated above, humans can not comprehend things beyond three dimensions. So, if we have an n-dimensional dataset, the only solution left to us is to create either a 2-D or 3-D graph out of it. Let’s say for simplicity, we are creating 2-D graphs. Suppose we have 1000 features in the dataset. That results in a  total (1000*999)/2= 499500 combinations possible for creating the 2-D graph.

Is it humanly possible to analyse all those graphs to understand the relationship between the variables?

**The questions that we need to ask at this point are:**

* Are all the features really contributing to decision making?
* Is there a way to come to the same conclusion using a lesser number of features?
* Is there a way to combine features to create a new feature and drop the old ones?
* Is there a way to remodel features in a way to make them visually comprehensible?

The answer to all the above questions is- _Dimensionality Reduction technique._


![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)


> ### Issue 1
> * Specifically the issue of data sparsity and “closeness” of data.
> * It becomes very challenging to identify meaningful patterns while analyzing and visualizing the data and it also degrades the Machine Learning model’s accuracy while decreasing the computation speed as well, i.e. training the model will become much slower as the dimensions increase.
> * Infinite Features Requires Infinite Training.

> ### Issue 2
> * In theory, one solution to the curse of dimensionality could be to increase the size of the training set to reach a sufficient density of training instances.
> * Unfortunately, in practice, the number of training instances required to reach a given density grows exponentially with the number of dimensions. 
 
 
 ### How to combat CoD
 ![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
 * **Dimensionality Reduction**
 * **Regularisation**
 * **Principal Component Analysis(PCA)**

### What is Dimensionality Reduction
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* In simple words, dimensionality reduction refers to the technique of reducing the dimension of a data feature set.
* Usually, machine learning datasets (feature set) contain hundreds of columns (i.e., features) or an array of points, creating a massive sphere in a three-dimensional space.
* By applying dimensionality reduction, you can decrease or bring down the number of columns to quantifiable counts, thereby transforming the three-dimensional sphere into a two-dimensional object (circle). 
> #### Approachs
* There are two main approaches to reducing dimensionality:
  - Projection.
  - Manifold Learning.

### Projection
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* In most real-world problems, training instances are not spread out uniformly across all dimensions. 
* Many features are almost **_constant_**, while others are **_highly correlated_** (as we can see in MNIST some consecutive pixels are identical). 
* As a result, all training instances lie within (or close to) a much lower-dimensional subspace of the high-dimensional space.( 2D space or 3D space in CNN for example)

### Manifold Learning
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

### Dimensionality Reduction benefits
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* It eliminates noise and redundant features.
* Handles Multicolinearity.
* It helps improve the model’s accuracy and performance. 
* It facilitates the usage of algorithms that are unfit for more large dimensions. 
* It reduces the amount of storage space required (less data needs lesser storage space).
* It compresses the data, which reduces the computation time and facilitates faster training of the data.  

### Where to use
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* It Works on Statistical Concept based Machine Learning Algorithms
  * Random forest doesnot need Dimensionality Reduction
  * Although Neural Net doesnot works very good but doesnot need Dimensionality Reduction.
 
### Dimensionality Reduction Techniques
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Dimensionality reduction techniques can be categorized into two broad categories:

### 1. Feature selection
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

The feature selection method aims to find a subset of the input variables (that are most relevant) from the original dataset. Feature selection includes three strategies, namely:

* Filter strategy
* Wrapper strategy 
* Embedded strategy 

### 2. Feature extraction
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
*  Principal Component Analysis (PCA)
*  Non-negative matrix factorization (NMF)
*  Linear discriminant analysis (LDA)
*  Generalized discriminant analysis (GDA)
*  Missing Values Ratio
*  Low Variance Filter
*  High Correlation Filter
*  Backward Feature Elimination
*  Forward Feature Construction
*  Random Forests




## References
* [Upgrad](https://www.upgrad.com/blog/top-dimensionality-reduction-techniques-for-machine-learning/)
