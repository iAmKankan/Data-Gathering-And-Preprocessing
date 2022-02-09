## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
* [RESTful API](url)
  * Falsk
## Setup
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
> ### Step 01: Install Virtual Environment
* Open a IDE 
* Go to the terminal
```Python3
$ pip install virtualenv
```
> ### Step 02: Now, create a new virtual environment as _my_Environment_.
 ```Python3
 $ virtualenv my_Environment
 ```
> ### Step 03: Then run the command:
  ``` Python 
  $ .\my_Environment\Scripts\activate  
  ```
  
> ### Step 04: Then install the dependencies: _Requirements.txt_ 
 ```Python3 
 $ (my_Environment) pip install -r requirements.txt
 ```
> ### Step 05: Finally start the web server:
 ```Python3
 $ (my_Environment) python app.py
 ```
> ### This server will start on port 5000 by default. You can change this in _app.py_ by changing the following line to this:
```Python3
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
### Example 01:
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* [app.py](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/blob/main/Deployment/app.py)
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
