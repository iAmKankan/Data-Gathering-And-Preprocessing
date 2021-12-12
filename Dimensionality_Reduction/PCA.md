## Principal Component Analysis(PCA)
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Principal Component Analysis (PCA) is by far the most popular dimensionality reduction algorithm. 
> #### First it identifies the hyperplane that lies closest to the data, and then it projects the data onto it

* It Works on Statistical Concept based Machine Learning Algorithms
  * Random forest does not need it.
  * It autometically handles [Multi-colinearity.](https://github.com/iAmKankan/MachineLearning_With_Python/blob/master/Supervised/Linear%20Regrassion/correlation.md) present in data.
  * It is sensitive to Outliers.

### Preserving the Variance
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Before you can project the training set onto a lower-dimensional hyperplane, you first need to choose the _**right hyperplane**_.
> #### For example,
* a simple 2D dataset is represented on the left, along with three different axes (i.e., 1D hyperplanes). 
* On the right is the result of the projection of the dataset onto each of these axes. 
* As you can see, the projection onto the solid line preserves the maximum variance, while the projection onto the dotted line preserves very little variance and the projection onto the dashed line preserves an intermediate amount of variance. 
<img src="https://user-images.githubusercontent.com/12748752/145732472-86499fae-d874-4c90-b175-fed040f4fffa.png" width=40% />
* It seems reasonable to select the axis that preserves the _maximum amount of variance_, as it will most likely lose less information than the other projections.
* Another way to justify this choice is that it is the axis that minimizes the mean squared distance between the original dataset and its projection onto that axis. 
* This is the rather simple idea behind PCA
