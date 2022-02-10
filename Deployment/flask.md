## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* Falsk setup

### [Example 01:](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/app.py)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
```python
from flask import Flask

app = Flask(__name__) # referencing this file

@app.route('/')
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)
```

### [Example 02:](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/app2.py)
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* [app.py]()
 
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

