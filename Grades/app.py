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


@app.route('/homework')
def render_homework_page():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT task, difficulty, subject, description FROM Homework"
    cur = con.cursor()
    cur.execute(query)
    homework_list = cur.fetchall()
    con.close()
    print(homework_list)
    return render_template('homework.html', homeworks=homework_list)


@app.route('/assign')
def render_assign_page():  # put application's code here
    con = create_connection(DATABASE)
    query = "SELECT a.id, name , task, due_date, completed, last_name FROM Assigned a " \
            "INNER JOIN Student s ON s.id = a.name_id " \
            "INNER JOIN Homework  h ON h.id =  a.homework_id"
    cur = con.cursor()
    cur.execute(query)
    assigned_homework_list = cur.fetchall()
    con.close()
    print(assigned_homework_list)
    return render_template('assigned.html', assignedhomeworks=assigned_homework_list)


if __name__ == '__main__':
    app.run()
