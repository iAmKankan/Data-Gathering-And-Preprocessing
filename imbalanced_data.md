## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

## What is Imbalanced data?
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
> #### Imbalanced data typically refers to a classification problem where the number of observations per class is not equally distributed; often you'll have a large amount of data/observations for one class (referred to as the majority class), and much fewer observations for one or more other classes (referred to as the minority classes).

## Handling Imbalanced Data for Classification
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)



## Balanced vs Imbalanced Dataset 
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* **Balanced Dataset:** In a Balanced dataset, there is approximately equal distribution of classes in the target column.
* **Imbalanced Dataset:** In an Imbalanced dataset, there is a highly unequal distribution of classes in the target column.

> ### Case 1:
> * If there are 900 ‘Yes’ and 100 ‘No’ then it represents an Imbalanced dataset as there is highly unequal distribution of the two classes. .


> ### Case 2:
> * If there are 550 ‘Yes’ and 450 ‘No’ then it represents a Balanced dataset as there is approximately equal distribution of the two classes.
> *  Hence, there is a significant amount of difference between the sample sizes of the two classes in an Imbalanced Dataset


## Problem with Imbalanced dataset:
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Algorithms may get biased towards the majority class and thus tend to predict output as the majority class.
* Minority class observations look like noise to the model and are ignored by the model.
* Imbalanced dataset gives misleading accuracy score.


## Techniques to deal with Imbalanced dataset :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

### Under Sampling :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* In this technique, we reduce the sample size of Majority class and try to match it with the sample size of Minority Class.
* **Example** : Let’s take an imbalanced training dataset with 1000 records.

#### Before Under Sampling :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* Target class ‘Yes’ = 900 records
* Target class ‘No’ = 100 records

#### After Under Sampling :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* Target class ‘Yes’ = 100 records
* Target class ‘No’ = 100 records
* Now, both classes have the same sample size.

> #### Pros :
> * Low computation power  needed.

> #### Cons :
> * Some important patterns might get lost due to dropping of records.
> * Only  beneficial for huge datasets with millions of records.
> * **Note** : Under Sampling should only be done when we have huge number of records.

### Over Sampling :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* In this technique, we increase the sample size of Minority class by replication and try to match it with the sample size of Majority Class.
* **Example**: Let’s take the same imbalanced training dataset with 1000 records.

#### Before Over Sampling :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Target class ‘Yes’ = 900 records
* Target class ‘No’ = 100 records

#### After Over Sampling :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

* Target class ‘Yes’ = 900 records
* Target class ‘No’ = 900 records

> #### Pros :
> * Patterns are not lost which enhances the model performance.

> #### Cons :
> * Replication of the data can lead to overfitting.
> * High computation power  needed.


### So, Which one to choose ‘Under Sampling’ or ‘Over Sampling’ ?
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* It depends upon the dataset. 
* If we have a huge dataset then choose ‘Under sampling’ otherwise go with ‘Over Sampling’.

### Using Tree Based Models :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* ‘Tree-based models’ find it easy to deal with Imbalanced dataset compared to Non-tree based Models due to their hierarchical structure.

#### Different Tree Based Models are :
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Decision Trees
* Random Forests
* Gradient Boosted Trees
### Using Anomaly Detection Algorithms:
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Anomaly or Outlier Detection algorithms are ‘one class classification algorithms’ that helps in identifying outliers ( rare data points) in the dataset.
* In an Imbalanced dataset, assume  ‘Majority class records as Normal data’ and ‘Minority Class records as Outlier data’.
* These algorithms are trained on Normal data.
* A trained model can predict if the new record is Normal or Outlier.


### How to detect an imbalanced class






