from io import open


class NoteClass(object):
    @staticmethod
    def saveNote(file, data):
        f = open('/Users/rakaz/Documents/GitHub/SwissArmyAssistant/static/media/Documents/'+file, "w", newline='')
        f.write("%s" % data)
        f.close()
        return

    @staticmethod
    def loadNote(file):
        try:  # crash proofing if file does not exist
            open('/Users/rakaz/Documents/GitHub/SwissArmyAssistant/static/media/Documents/'+file, "r", newline='')
        except FileNotFoundError:
            data = "file not found!"
            return data

        f = open('/Users/rakaz/Documents/GitHub/SwissArmyAssistant/static/media/Documents/'+file, "r", newline='')
        data = "null"

        if f.mode == 'r':
            data = f.read()
        return data


