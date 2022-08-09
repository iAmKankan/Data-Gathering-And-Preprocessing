## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
#### Project Setup
* [Virtual Environment](#virtual-environment)
* Requirements setup 

#### _Micro-Web frameworks in Python_ 
  * [Falsk](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/tree/main/Deployment/flask)
#### _Cloud Plateforms_
  * [Heroku](https://github.com/iAmKankan/Data-Gathering-And-Preprocessing/tree/main/Deployment/heroku#readme)

<img src="https://user-images.githubusercontent.com/12748752/154287300-f19161fc-ada0-4c38-8920-422ad688065a.png" weight=40% />

![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)
## Micro-Web frameworks in Python 
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
* There are many frameworks which allow building your webpage using python like a **_bottle_**, **_Django_**, **_flask_**, etc. 
* But the real popular ones are **_Flask_** and **_Django_**.
* Django is easy to use as compared to Flask but Flask provides you the versatility to program with.

## Virtual Environment 
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)
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
