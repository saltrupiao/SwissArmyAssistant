import os
from flask import request
import log


def setFilePath(folder):

    if folder == "Documents":
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media/Documents'
    elif folder == "Pictures":
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media/Pictures'
    elif folder == "Music":
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media/Music'
    elif folder == "none":
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media'
    else:
        path = "Error"
    #log.writeLog("Path set to " + path)

    return path


def upload(path):
    #path = setFilePath()
    target = path
    print(target)

    for file in request.files.getlist("files"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)


def dir_listing(path):
    # Show directory contents
    files = os.listdir(path)
    return files
