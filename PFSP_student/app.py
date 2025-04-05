from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_db"
)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']

    cursor.execute("INSERT INTO students (name, email, course) VALUES (%s, %s, %s)", (name, email, course))
    conn.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
