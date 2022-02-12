## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Basic Flask
## Basic Flask 
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* **_Flask_** and **_Flask-RESTful_**
#### [Example 01:](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/app.py)
 ```python
from flask import Flask

app = Flask(__name__) # referencing this file

@app.route('/')
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)
```

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

> * ####  Save this as api.py and run it using your Python interpreter. And open 'localhost' with port 5000 - "http://127.0.0.1:5000/" or "http://localhost:5000/".
> * #### _Note_ that we’ve enabled Flask debugging mode to provide code reloading and better error messages.
> * ####  _Debug mode should never be used in a production environment!_

### Static Content
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* Make `index.html` file inside `templates` folder.
* Make change in the python code that will return a html file not a string `return render_template('index.html', tasks=tasks)`
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
### Template Inheritance
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

## Resources:
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [Flask doc](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
* [Geeksforgeeks-Template Inheritance](https://www.geeksforgeeks.org/template-inheritance-in-flask/)
