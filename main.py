from flask import Flask, render_template, request
from CalcClass import CalcClass
from NoteClass import NoteClass
from file import dir_listing, setFilePath, upload, setShortFilePath, getLastModified
from music import dir_listing_music, setFilePathMusic
from theme import getTheme, setTheme
from log import writeLog

# Placeholder for the application
app = Flask(__name__)

#APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def firstLoad():
    return hello_world()

# This tells our program the route to our server
@app.route('/home')
def hello_world():
    theme = getTheme()
    return render_template('home.html', theme = theme)


@app.route('/about')
def about():
    theme = getTheme()
    return render_template('about.html', theme = theme)

@app.route('/settheme', methods=['POST'])
def themeChange():
    writeLog('Setting theme')
    page = setTheme()
    return page

@app.route('/calc')
def calcpage():
    theme = getTheme()
    return render_template('calc.html', theme = theme)


@app.route('/calc', methods=['POST'])
def calc():
    theme = getTheme()
    inp = request.form['display']  # pull expression from text field
    result = CalcClass.calculation(inp)
    return render_template('calc.html', result=result, theme = theme)  # sends result to page


# https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
@app.route('/home', methods=['POST'])
def my_form_post():
    theme = getTheme()
    text = request.form['txt']
    new_text = "You entered the word " + text
    return render_template('home.html', new_text = new_text, theme = theme)


@app.route('/note')
def notepad():
    theme = getTheme()
    return render_template('note.html', text = "New Note", fn="Enter filename for save", theme = theme)


@app.route('/note', methods=['POST'])
def noteFunctions():
    theme = getTheme()
    ans = request.form['tag']  # determine which submit button was pressed
    if ans == "Save":
        filename = request.form['filename']
        data = request.form['notepad']
        NoteClass.saveNote(filename, data)
        return render_template('note.html', text=data, fn=filename, theme = theme)
    if ans == "Load":
        filename = request.form['filename']
        data = NoteClass.loadNote(filename)
        return render_template('note.html', text=data, fn=filename, theme = theme)
    if ans == "reset":
        return render_template('note.html', text="New Note", fn="Enter filename for save", theme = theme)


@app.route('/files', methods=['GET', 'POST'])
def file():
    theme = getTheme()
    tag = request.form.get('folder')

    path = setFilePath(tag)
    writeLog("Getting path")
    writeLog("Path: " + path)

    shortPath = setShortFilePath(tag)
    writeLog("Getting Short Path")
    writeLog("Short Path: " + shortPath)

    lastMod = getLastModified(tag)

    if request.method == 'POST':
        writeLog("Method is POST")
        if "upload" in request.form:
            writeLog("Calling Upload Function")
            upload(tag)
        elif "view" in request.form:
            writeLog("Calling View Function")
            path = setFilePath(tag)

    files = dir_listing(path)



    if tag == None:
        tag = "Documents"

    return render_template('upload.html', files = files, path = tag, shortPath = shortPath, theme = theme, lastMod = lastMod)

@app.route('/music')
def music():
    # These functions are a straight ripped from file.py and modified for music player functionality
    theme = getTheme()
    mtag = request.form.get('folder')
    path = setFilePathMusic(mtag)
    if request.method == 'POST':
        if "upload" in request.form:
            upload(mtag)
        elif "view" in request.form:
            path = setFilePathMusic(mtag)

    files = dir_listing_music(path)

    if mtag == None:
        tag = "Music"

    theme = getTheme()
    return  render_template('music.html', files = files, path = tag, theme = theme)

@app.route('/news')
def news():
    theme = getTheme()
    return render_template('news.html', theme = theme)


@app.route('/game')
def game():
    theme = getTheme()
    return render_template('game.html', theme = theme)


if __name__ == '__main__':
    app.run(debug=True) # so the page refreshes live and doesn't need to be restarted

