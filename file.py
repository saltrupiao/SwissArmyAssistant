import os
from flask import request
from log import writeLog


def setFilePath(folder):
    #Get the root of this python file
    root = os.path.dirname(os.path.abspath(__file__))
    writeLog("Root: " + root)

    if folder is None:
        # If the user just loaded the page there won't be a directory, so documents is default
        folder = "Documents"
        writeLog("Directory: " + folder)

    # Add the /static/media path to the full path
    path = root + '/static/media/' + folder
    writeLog("Path: " + path)

    return path


def upload(tag):
    writeLog("Upload - setting upload path")
    path = setFilePath(tag)
    writeLog("Upload path " + path)

    for file in request.files.getlist("files"):
        writeLog("Uploading file")
        print(file)
        writeLog("File: " + str(file))
        filename = file.filename
        destination = "/".join([path, filename])
        writeLog("Destination: " + destination)
        print(destination)
        writeLog("Destination: " + destination)
        file.save(destination)


#    file = request.files['file']
#    if file:
#        file.save('/where/to/save', file.filename)



def dir_listing(path):
    # Show directory contents
    files = os.listdir(path)
    return files