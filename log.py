from datetime import datetime


def writeLog(logText):
    stamp = datetime.now()
    logLocation = "/var/log/SwissArmyAssistant/debug.log"
    log = open(logLocation, "a")
    log.write(stamp + " - " + logText)
    log.write("\n")
