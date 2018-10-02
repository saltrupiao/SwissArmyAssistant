from flask import Flask, render_template, request


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


if __name__ == '__main__':
    app.run(debug=True) # so the page refreshes live and doesn't need to be restarted
