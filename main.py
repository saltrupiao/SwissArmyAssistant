from flask import Flask, render_template, request, redirect, url_for, flash
from CalcClass import CalcClass
from NoteClass import NoteClass
from file import dir_listing, setFilePath, upload
from log import writeLog

# Placeholder for the application
app = Flask(__name__)

#app.config['TRAP_BAD_REQUEST_ERRORS'] = True
#app.config['DEBUG'] = True

# This tells our program the route to our server
@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/calc')
def calcpage():
    return render_template('calc.html')


@app.route('/calc', methods=['POST'])
def calc():
    inp = request.form['display']  # pull expression from text field
    result = CalcClass.calculation(inp)
    return render_template('calc.html', result=result)  # sends result to page


# https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['txt']
    new_text = "You entered the word " + text
    return render_template('home.html', new_text = new_text)


@app.route('/note')
def notepad():
    return render_template('note.html', text = "New Note", fn="Enter filename for save")


@app.route('/note', methods=['POST'])
def noteFunctions():
    ans = request.form['tag']  # determine which submit button was pressed
    if ans == "Save":
        filename = request.form['filename']
        data = request.form['notepad']
        NoteClass.saveNote(filename, data)
        return render_template('note.html', text=data, fn=filename)
    if ans == "Load":
        filename = request.form['filename']
        data = NoteClass.loadNote(filename)
        return render_template('note.html', text=data, fn=filename)
    if ans == "reset":
        return render_template('note.html', text="New Note",
                               fn="Enter filename for save")

@app.route('/files', methods=['GET', 'POST'])
def file():
    tag = request.form.get('folder')

    path = setFilePath(tag)
    writeLog("Getting path")
    writeLog("Path: " + path)

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

    return render_template('upload.html', files = files, path = tag)


@app.route('/music')
def music():
    return render_template('music.html')


if __name__ == '__main__':
    app.run(debug=True) # so the page refreshes live and doesn't need to be restarted
