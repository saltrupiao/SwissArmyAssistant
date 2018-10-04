from io import open


class NoteClass(object):
    @staticmethod


        f.write("%s" % data)
        f.close()
        return

    @staticmethod

    def loadNote(file):
        try:  # crash proofing if file does not exist
            open(file+".txt", "r", newline='')
        except FileNotFoundError:
            data = "file not found!"
            return data

        f = open(file+".txt", "r", newline='')
        data = "null"

        if f.mode == 'r':
            data = f.read()
        return data


