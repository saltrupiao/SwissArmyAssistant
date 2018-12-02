import os, sys, time
from flask import request
from log import writeLog


#https://docs.python.org/3/library/datetime.html
from datetime import datetime

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


def setShortFilePath(folder):
    if folder is None:
        # If the user just loaded the page there won't be a directory, so documents is default
        folder = "Documents"
        writeLog("Directory: " + folder)

    # Add the /static/media path to the full path
    shortPath = '/static/media/' + folder + '/'
    writeLog("Path: " + shortPath)

    return shortPath

def getLastModified(tag):
    path = setFilePath(tag)
    print("File Path: " + path)

    #------------------References for Loop Functionality in file.py and upload.html--------------------------
    #https://stackoverflow.com/questions/38943625/how-to-use-getmtime-for-multiple-files
    #https://stackoverflow.com/questions/31487732/simple-way-to-drop-milliseconds-from-python-datetime-datetime-object
    #https://stackoverflow.com/questions/7537439/how-to-increment-a-variable-on-a-for-loop-in-jinja-template
    #https://stackoverflow.com/questions/9486393/jinja2-change-the-value-of-a-variable-inside-a-loop
    #https://stackoverflow.com/questions/38509802/get-the-current-and-next-value-in-a-jinja-for-loop
    #https://stackoverflow.com/questions/17691838/range-in-jinja2-inside-a-for-loop

    file_list = []

    for file in os.listdir(path):
        fileToIndex = os.path.join(path, str(file))
        mTime = os.path.getmtime(fileToIndex)
        mTimeFmt = datetime.fromtimestamp(mTime).strftime('%Y-%m-%d %H:%M:%S')
        curFile = str(file)

        file_list.append(curFile)
        file_list.append(mTimeFmt)

    return file_list


def dir_listing(path):
    # Show directory contents
    files = os.listdir(path)

    return files