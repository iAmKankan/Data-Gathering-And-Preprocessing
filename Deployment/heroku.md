## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

## Heroku 
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.[3] For this reason, Heroku is said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most languages. Heroku was acquired by Salesforce.com in 2010 for $212 million.

### Setup
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
> ### Step 01: local Project folder
* We need to add two files inorder to deploy the project on cloud
  * File name **_`Procfile`_** ( generic file - no file extention)
  * File name **_`runtime.txt`_**
> #### **_`Procfile`_** contains
```python
web: gunicorn app:app
```

> #### **_`runtime.txt`_** contains
```python
python-3.7.10
```
> ### Step 02: Heroku setup
* Login in Heroku site 
* Give a  name of the project lets say **_`grescorepredic01`_**
* Choose any **`Deployment method`**
* And follow the steps accordingly.

