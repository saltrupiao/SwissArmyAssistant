from flask import Flask, render_template, request
from CalcClass import CalcClass
from NoteClass import NoteClass

# Placeholder for the application
app = Flask(__name__)


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

    try:  # Data validation, will prevent program crash if user enters invalid expression
        eval(inp)
    except ZeroDivisionError:  # Ex: 8/0
        result = 'Error: Divide by Zero'
        return render_template('calc.html', result=result)
    except NameError:  # Ex: a+1
        result = 'Error: Check your syntax'
        return render_template('calc.html', result=result)
    except SyntaxError:  # Ex: 3a+1, 3-+
        result = 'Error: Check your syntax'
        return render_template('calc.html', result=result)

    result = eval(inp)  # builds string result from the evaluation of user input expression

    if isinstance(result, float):
        result = round(result, 3)

    return render_template('calc.html', result=result)  # sends result to page


# https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['txt']
    new_text = "You entered the word " + text
    return render_template('home.html', new_text = new_text)


@app.route('/note')
def notepad():
    return render_template('note.html', text = "New Note", fn="Enter filename to save or load (refrain from typing .txt)")


@app.route('/note', methods=['POST'])
def noteFunctions():
    ans = request.form['tag']  # determine which submit button was pressed
    filename = request.form['filename']
    if ans == "Save":
        data = request.form['notepad']
        NoteClass.saveNote(filename, data)
        return render_template('note.html', text=data, fn=filename)
    if ans == "Load":
<<<<<<< HEAD
        data = NoteClass.loadNote(filename)
        return render_template('note.html', text=data, fn=filename)

=======
        data = NoteClass.loadNote()
        return render_template('note.html', text=data)
>>>>>>> 53fbbde85f5f7f5d97b0e427baf9b5202632a657

if __name__ == '__main__':
    app.run(debug=True) # so the page refreshes live and doesn't need to be restarted

