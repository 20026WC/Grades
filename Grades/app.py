from flask import Flask, render_template
import sqlite3
from sqlite3 import Error

DATABASE = 'C:/Users/riley/OneDrive/DTS/13DTS/Flask/gradesProject/Grades/grades.db'
app = Flask(__name__)


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
    return None


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
