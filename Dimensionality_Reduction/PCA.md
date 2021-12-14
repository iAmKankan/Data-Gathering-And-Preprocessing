## Principal Component Analysis(PCA)
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
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

### Principal Components
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* **_PCA identifies the axis that accounts for the largest amount of variance in the training set_**. (in the figure, it is the solid line)
* Which the first Principle Component(PC) on which the vector C<sub>1</sub> lies.
* It also finds a second axis, orthogonal(Perpendicular) to the first one, that accounts for the largest amount of remaining variance. (in this 2D example there is no choice: it is the dotted line)
* Similarly it is the socond Principle Component(PC) on which the vector C<sub>2</sub> lies.
* If it were a higher-dimensional dataset, PCA would also find a third axis, orthogonal to both previous axes, and a fourth, a fifth, and so on—as many axes as the number of dimensions in the dataset.
* The third PC would be the axis orthogonal to that plane where the first two PC were axis orthogonal to each other.
> #### So how can you find the principal components of a training set? 
* Luckily, there is a standard matrix factorization technique called _Singular Value Decomposition (SVD)_ that can decompose the training set matrix X into the matrix multiplication of three matrices U Σ V ,

> #### Linear dimensionality reduction using Singular Value Decomposition of the data to project it to a lower dimensional space. The input data is centered but not scaled for each feature before applying the SVD.
## References
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Hands-on ML by Aurelien Geron
