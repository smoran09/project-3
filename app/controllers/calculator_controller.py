from app.app import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'Value 1 and value 2 must be entered'
        else:
            flash('You have successfully calculated')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # making the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator.html')
