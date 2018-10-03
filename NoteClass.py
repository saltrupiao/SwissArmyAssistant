from io import open


class NoteClass(object):
    @staticmethod
    def saveNote(data):
        f = open("note.txt", "w", newline='')
        f.write("%s" % data)
        f.close()
        return

    @staticmethod
    def loadNote():
        f = open("note.txt", "r", newline='')
        data = "null"
        if f.mode == 'r':
            data = f.read()
        return data


