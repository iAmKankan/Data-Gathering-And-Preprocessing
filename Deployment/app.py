from flask import Flask

app = Flask(__name__) # referencing this file

@app.route('/')
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)