import os
from flask import request
import log


def setFilePath():
    folder = request.form['folder']
    if folder == "Documents":
        path = '/home/connor/Documents/smproject/SwissArmyAssistant/static/media/Documents'
    elif folder == "Pictures":
        path = '/home/connor/Documents/smproject/SwissArmyAssistant/static/media/pictures'
    elif folder == "Music":
        path = '/home/connor/Documents/smproject/SwissArmyAssistant/static/media/music'
    else:
        path = "Error"
    log.writeLog("Path set to " + path)

    return path


def upload(APP_ROOT):
    path = setFilePath()
    target = os.path.join(APP_ROOT, path)
    print(target)

    if not os.path.isdir(target):
        log.writeLog("Creating new directory " + target)
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


