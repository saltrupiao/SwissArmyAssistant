from flask import render_template, request


class CalcClass(object):
    @staticmethod
    def calculation(inp):

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

        return result
