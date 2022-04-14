## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)

## Heroku 
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.[3] For this reason, Heroku is said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most languages. Heroku was acquired by Salesforce.com in 2010 for $212 million.

### Setup
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
> ### Step 01: local Project folder
* We need to add three files inorder to deploy the project on cloud
  * File name **_`Procfile`_** ( generic file - no file extention)
  * File name **_`runtime.txt`_**
  * File name **_`requirements.txt`_**
> #### [**_`Procfile`_**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/Procfile) contains
```python
web: gunicorn app:app
```

> #### [**_`runtime.txt`_**](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/runtime.txt) contains
```python
python-3.7.10
```
> #### [**_`requirements.txt`_**]
```Python
certifi==2019.11.28
Click==7.0
Flask==1.1.2
Flask-Cors==3.0.9
Flask-WTF==1.0.1
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.10.3
joblib==0.14.0
MarkupSafe==1.1.1
numpy==1.17.4
scikit-learn==0.21.3
scipy==1.3.2
six==1.13.0
Werkzeug==1.0.1
WTForms==3.0.0
```
> ### Step 02: Heroku setup
* Login in Heroku site 
* Give a  name of the project lets say **_`grescorepredic01`_**
* Choose any **`Deployment method`**
* And follow the steps accordingly.

