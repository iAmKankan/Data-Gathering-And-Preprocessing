## Index
![Dark](https://user-images.githubusercontent.com/12748752/126914729-75e0fed5-fdaa-4216-81c8-719340e80694.png)



### Basic **_Flask_** Upload files:
![Light](https://user-images.githubusercontent.com/12748752/126914730-b5b13ba9-4d20-4ebf-b0ed-231af4c8b984.png)

```Python
from flask import Flask, render_template, redirect, flash

app =  Flask(__name__)

@app.route('/')

def index():
    return reder_template('index.html')
```
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>files in flask</title>
</head>
<body>
    <div class="container">
        <h1>Upload your files here</h1>
        <p>Upload only text, json files only.</p>
        
        <form action="/" method="post" enctype="multipart/form-data"> 
        <!-- We have created a form, The action would be '/' in flask we declaired-->
          <input type="file" name="file" required multiple>
          <input type="submit" value="Upload">
        </form>
    
     </div>
    
</body>
</html>
```
<img src="https://user-images.githubusercontent.com/12748752/162966501-1c14e621-3fa3-463f-9207-e38bfa2dea21.png" width=50%/>
