from datetime import datetime
from file import setFilePath


def writeLog(logText):
    stamp = datetime.now()
    logLocation = setFilePath('log')
    log = open(logLocation, "a")
    log.write(str(stamp) + " - " + str(logText))
    log.write("\n")
