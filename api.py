#!/usr/bin/python3
import os
from flask import Flask, render_template, request, redirect
import src.predict as p
import src.upload as u

api = Flask(__name__)

@api.route("/", methods=["GET","POST"])
def main():
    return render_template('index.html')

@api.route('/upload', methods=['POST'])
def upload():
    category = u.do_upload()
    return render_template('{}.html'.format(category))

@api.route('/post', methods=['POST'])
def postman():
    return {"Category": u.do_post()}

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=80, debug=True)

