from datetime import datetime
import os


def setFilePath():
    # Get the root of this python file
    root = os.path.dirname(os.path.abspath(__file__))
    path = root + '/log/debug.log'

    return path

logLocation = setFilePath()

def writeLog(logText):
    stamp = datetime.now()
    log = open(logLocation, "a")
    log.write(str(stamp) + " - " + str(logText))
    log.write("\n")