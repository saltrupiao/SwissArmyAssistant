import os
from flask import request


def setFilePath():
    usrpath = request.form['txtpath']
    if usrpath is None:
        path = "/home/connor/smproject/SwissArmyAssistant/static/media"
    else:
       path = usrpath

    return path


def upload(APP_ROOT):
    path = setFilePath()
    target = os.path.join(APP_ROOT, path)
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)


def dir_listing(path):
    # Show directory contents
    files = os.listdir(path)
    return files


