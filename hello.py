from flask import Flask, render_template, Markup
import os
import json

app = Flask(__name__)

COLOR = "#33CC33"

# get CF environment variables
port = int(os.getenv("PORT", "8080"))

content = '<h1>Hello World!</h1></br>I am a python builpack application'
content = Markup(content)

@app.route('/')
def hello_world():
    return render_template("index.html",bgcolor=COLOR,content=content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
