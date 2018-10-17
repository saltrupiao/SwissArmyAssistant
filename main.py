import os, log
from flask import Flask, render_template, request
from CalcClass import CalcClass
from NoteClass import NoteClass
from file import dir_listing, setFilePath, upload

# Placeholder for the application
app = Flask(__name__)

#APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_ROOT = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media'
print(APP_ROOT)

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
    if request.method == 'POST':
        tag = request.form.get('folder')
        print(tag)
        newAppRoot = APP_ROOT + '/' + tag
        print("newAppRoot: " + newAppRoot)
        if "upload" in request.form:
            path = setFilePath(tag)
            upload(newAppRoot)
        elif "view" in request.form:
            path = setFilePath(tag)


    if request.method == 'GET':
        path = '/Users/saltrupiano/PycharmProjects/SwissArmyAssistant/static/media/'

    #dir_listing(path)
    files = dir_listing(path)


    return  render_template('upload.html', files = files, path = path)




#@app.route('/upload', methods=['GET', 'POST'])
#def upload():
#    target = os.path.join(APP_ROOT, '/Users/saltrupiano/Desktop')
#    print(target)

#    if request.method == 'POST':
#        f = request.files[file]
#        f.save(request.files['file'])
#        return 'file uploaded successfully'
# break
#   -----------------
#     if not os.path.isdir(target):
#         os.mkdir(target)
#
#     for file in request.files.getlist("file"):
#         print(file)
#         filename = file.filename
#         destination = "/".join([target, filename])
#         print(destination)
#         file.save(destination)


@app.route('/Music')
def music():
    return render_template('Music.html')


if __name__ == '__main__':
    app.run(debug=True) # so the page refreshes live and doesn't need to be restarted

