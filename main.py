from flask import Flask, render_template, request
from CalcClass import CalcClass
from NoteClass import NoteClass
import os.path



# Placeholder for the application
app = Flask(__name__, static_url_path='/static')


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
    return render_template('note.html', text = "New Note")


@app.route('/note', methods=['POST'])
def noteFunctions():
    ans = request.form['tag']
    if ans == "Save":
        data = request.form['notepad']
        NoteClass.saveNote(data)
        return render_template('note.html', text=data)
    if ans == "Load":
        data = NoteClass.loadNote()
        return render_template('note.html', text=data)


# @app.route('/note', methods=['POST'])
# def loadNote():
#     data = NoteClass.loadNote()
#     return render_template('note.html', text=data)


if __name__ == '__main__':
    app.run(debug=True)  # so the page refreshes live and doesn't need to be restarted
