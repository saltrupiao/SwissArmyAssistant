import os
from flask import request


def setFilePath(folder):

    if folder == "Documents":
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media/Documents'
    elif folder == "Pictures":
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media/pictures'
    elif folder == "Music":
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media/music'
    else:
        path = "Error"

    return path


def upload(path):
    path = setFilePath()
    target = path
    print(target)

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
