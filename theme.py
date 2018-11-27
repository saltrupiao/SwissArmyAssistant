from flask import make_response, render_template, request
from log import writeLog

def setTheme():
    theme = request.form['theme']
    writeLog('Theme requested is ' + str(theme))
    response = make_response(render_template('home.html', theme = theme))
    writeLog('Response created')
    response.set_cookie('theme', theme)
    writeLog('Cookie set to ' + str(theme))
    return response

def getTheme():
    writeLog('Getting theme')
    theme = request.cookies.get('theme')
    if theme is None:
        writeLog('Theme defaulted to blue')
        theme = 'blue'
    writeLog('theme cookie is ' + str(theme))
    return theme