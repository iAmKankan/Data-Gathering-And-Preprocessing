## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [The Curse of Dimensionality](#the-curse-of-dimensionality)
* [What is Dimensionality Reduction?](#what-is-dimensionality-reduction)
* [Dimensionality Reduction benefits](#dimensionality-reduction-benefits)
   * [1. Feature selection](#1-feature-selection)
   * [2. Feature extraction](#2-feature-extraction)
 * [Principal Component Analysis(PCA)](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Dimensionality_Reduction/PCA.md)

### The Curse of Dimensionality
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* The curse of dimensionality is a problem that arises when we are working with a lot of data having multiple features or we can say it as high dimensional data.
* The dimension of the data means the no. of features or columns in our dataset.
> ### Issues
> * Specifically the issue of data sparsity and “closeness” of data.
> * It becomes very challenging to identify meaningful patterns while analyzing and visualizing the data and it also degrades the Machine Learning model’s accuracy while decreasing the computation speed as well, i.e. training the model will become much slower as the dimensions increase.
> * Infinite Features Requires Infinite Training.

> ### Solution 1
> * In theory, one solution to the curse of dimensionality could be to increase the size of the training set to reach a sufficient density of training instances.
> * Unfortunately, in practice, the number of training instances required to reach a given density grows exponentially with the number of dimensions. 

### What is Dimensionality Reduction
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* In simple words, dimensionality reduction refers to the technique of reducing the dimension of a data feature set.
* Usually, machine learning datasets (feature set) contain hundreds of columns (i.e., features) or an array of points, creating a massive sphere in a three-dimensional space.
* By applying dimensionality reduction, you can decrease or bring down the number of columns to quantifiable counts, thereby transforming the three-dimensional sphere into a two-dimensional object (circle). 

### Dimensionality Reduction benefits
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* It eliminates noise and redundant features.
* Handles Multicolinearity.
* It helps improve the model’s accuracy and performance. 
* It facilitates the usage of algorithms that are unfit for more large dimensions. 
* It reduces the amount of storage space required (less data needs lesser storage space).
* It compresses the data, which reduces the computation time and facilitates faster training of the data.  
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

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
