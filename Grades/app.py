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
def render_homepage():  # put application's code here
    return render_template('home.html')


@app.route('/student')
def render_student_page():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT id, name, last_name, year_level, email, description FROM Student"
    cur = con.cursor()
    cur.execute(query)
    student_list = cur.fetchall()
    con.close()
    print(student_list)
    return render_template('student.html', students=student_list)


if __name__ == '__main__':
    app.run()
