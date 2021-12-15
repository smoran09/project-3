from app.app import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    @staticmethod
    def get():
        return render_template('index.html')
