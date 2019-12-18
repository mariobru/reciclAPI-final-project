from flask import Flask, render_template, request, redirect
import os
import src.predict as p

def do_upload():
    upload = request.files['upload']
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = "./new_test"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    imgname = str(upload.filename)
    prediction = p.predict(imgname)
    os.remove("./new_test/{}".format(imgname))
    return str(prediction)

def do_post():
    upload = request.files['post']
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = "./new_test"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path)
    imgname = str(upload.filename)
    prediction = p.predict(imgname)
    os.remove("./new_test/{}".format(imgname))
    return str(prediction)