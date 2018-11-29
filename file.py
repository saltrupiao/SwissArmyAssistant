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

    #https://stackoverflow.com/questions/38943625/how-to-use-getmtime-for-multiple-files
    # for file in os.listdir(path):
    #     fileToIndex = os.path.join(path, str(file))
    #     mTime = os.path.getmtime(fileToIndex)
    #     lastMod = datetime.fromtimestamp(mTime).replace(microsecond=0)
        #https://stackoverflow.com/questions/31487732/simple-way-to-drop-milliseconds-from-python-datetime-datetime-object

    #return lastMod

    # for file in dir_listing(path):
    #     fileToIndex = os.path.join(path, str(file))
    #     mTime = os.stat(fileToIndex).st_mtime
    #     lastMod = datetime.fromtimestamp(mTime).strftime('%Y-%m-%d %H:%M:%S')

    # lastMod = ""
    # fileandMod = ""
    # for file in os.listdir(path):
    #     fileToIndex = os.path.join(path, str(file))
    #     print(fileToIndex)
    #     mTime = os.path.getmtime(fileToIndex)
    #     print("mTime: " + str(mTime))
    #     curLastMod = datetime.fromtimestamp(mTime).strftime('%Y-%m-%d %H:%M:%S')
    #     curFile = str(file)
    #     fileandMod = curFile + ',' + curLastMod
    #
    #     lastMod += fileandMod + ','
    #     print(lastMod)





    file_list = []

    for file in os.listdir(path):
        fileToIndex = os.path.join(path, str(file))
        mTime = os.path.getmtime(fileToIndex)
        mTimeFmt = datetime.fromtimestamp(mTime).strftime('%Y-%m-%d %H:%M:%S')
        curFile = str(file)

        file_list.append(curFile)
        file_list.append(mTimeFmt)



    # file_list = []
    #
    # for i in directoryList:
    #     a = os.path.join(path, i)
    #     mTime = os.path.getmtime(a)
    #     file_list.append([datetime.fromtimestamp(mTime).strftime('%Y-%m-%d %H:%M:%S')])
    #
    # return file_list

    return file_list


def dir_listing(path):
    # Show directory contents
    files = os.listdir(path)

    return files