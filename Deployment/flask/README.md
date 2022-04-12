## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Basic Flask
## Flask 
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Flask is a micro-web application framework written in Python. 
* Flask is based on the Werkzeug **WSGI** toolkit and **Jinja2** template engine. 
* Both are Pocco projects.
* To understand what Flask is you have to understand few general terms. 
  * **_WSGI_** Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. WSGI is a specification for a universal interface between the web server and the web applications. 
  * **_Werkzeug_** It is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. The Flask framework uses Werkzeug as one of its bases.
  * **_jinja2_** jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.

### Basic **_Flask_** and **_Flask-RESTful_**
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

#### [Example 01:](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/app.py)
```python3

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__) # referencing this file

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')

# ‘/’ URL is bound with index() function.
def index():
    return "Hello world"

# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
```
#### Output
<img src="https://user-images.githubusercontent.com/12748752/162886709-40651c92-ff0b-47df-bb7a-02f1450140f3.png" width=50% style="padding:1px;border:thin solid black;" />

#### [Example 02:](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/app2.py)
 ```Python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
 ```
* Output
```python
{'hello': 'world'}
```

#### Output
<img src="https://user-images.githubusercontent.com/12748752/162887181-c8b48965-c76c-4ba4-b2eb-eb386880a9dd.png" width=40% border="1" />

* **Save this as api.py and run it using your Python interpreter. And open 'localhost' with port 5000 - "http://127.0.0.1:5000/" or "http://localhost:5000/".**
#### _Note_ 
* **We’ve enabled Flask debugging mode to provide code reloading and better error messages.**
* **_Debug mode should never be used in a production environment!_**

### Flask with Static Content
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Make **_`index.html`_** file inside **_`templates`_** folder.
* Make change in the python code that will return a _html_ file not a string - **`return render_template('index.html', tasks=tasks)`**
 > #### Python file
 ```python
from flask import Flask
app = Flask(__name__) # referencing this file
@app.route('/')
def index():
    return render_template('index.html') #return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)
```
> #### HTML file
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    Hello Wortld 2
</body>
</html>
```

#### Output
<img src="https://user-images.githubusercontent.com/12748752/162891973-f33ce7ce-2829-496b-8731-dfd0f1b91ef0.png" width=40%/>

### Template Inheritance
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Template inheritance is a very good feature of Jinja templating . Jinja is a web template engine for the Python programming language . 
* We have seen that webpages of a website contains same footer , navigation bar etc.  So instead of making same footer and navigation bar in all webpages separately , we make use of template inheritance , which allows us to create the part which is same in all webpages (eg. footer,navigation bar) only once and we also don’t need to write the html , head , title tag again and again . 
* Lets define the common structure of web pages in **_base.html_** file. First of all we will render  template using flask from _**main.py**_ file .

#### Step 1:
* Create a flask app to render the main template 

```Python

from flask import Flask, render_template
  
# Setting up the application
app = Flask(__name__)
  
# making route
  
  
@app.route('/')
def home():
    return render_template('home.html')
  
  
# running application
if __name__ == '__main__':
    app.run(debug=True)
```
#### Step 2 
* Create HTML Files
  * Now we will set up our **_base.html_** file in which we have one heading which will be common in all webpages. 

> #### Syntax : 
```
{% block content %}
{% endblock %}
```
* The code above and below these lines will be the same for every web pages and the code between them will be for a specific web page . 

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Template Inheritance</title>
</head>
<body>
    <h1> This heading is common in all webpages </h1>
    {% block content %}
    {% endblock %}
  
</body>
</html>
```

* Now we will set up our **_home.html_** file in which we will inherit template from **_"base.html"_** file and will write some code for home page as well . 

> #### Syntax :
```
        {% extends "base.html" %}
        {% block content %}
          write code here for home page only 
        {% endblock %}
```

```HTML
{%extends "base.html" %}
{%block content%}
  
<h1>Welcome to Home</h1>
  
{% endblock %}
```


## Resources:
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [Flask doc](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
* [Geeksforgeeks-Template Inheritance](https://www.geeksforgeeks.org/template-inheritance-in-flask/)
