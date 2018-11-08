from io import open


class NoteClass(object):
    @staticmethod
    def saveNote(file, data):
        f = open(file, "w", newline='')
        f.write("%s" % data)
        f.close()
        return

    @staticmethod
    def loadNote(file):
        try:  # crash proofing if file does not exist
            open(file, "r", newline='')
        except FileNotFoundError:
            data = "file not found!"
            return data

        f = open(file,"r", newline='')
        data = "null"

        if f.mode == 'r':
            data = f.read()
        return data


