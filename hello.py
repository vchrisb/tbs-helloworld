from flask import Flask, render_template, Markup
import os
import json

app = Flask(__name__)

COLOR = "#33CC33"

content = '<h1>Hello World!</h1></br>I am a python builpack application'
content = Markup(content)

@app.route('/')
def hello_world():
    return render_template("index.html",bgcolor=COLOR,content=content)
