
python
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('courses.db')
cursor = connection.cursor()

@app.route('/register', methods=['POST'])
def register():
name = request.form['name']
email = request.form['email']
phone = request.form['phone']
course = request.form['course']

cursor.execute("INSERT INTO registrations (name, email, phone, course) VALUES (?, ?, ?, ?)",
(name, email, phone, course))
connection.commit()

return redirect(url_for('success'))

@app.route('/courses')
def courses():
cursor.execute("SELECT * FROM courses")
courses = cursor.fetchall()

return render_template('courses.html', courses=courses)

@app.route('/instructors')
def instructors():
cursor.execute("SELECT * FROM instructors")
instructors = cursor.fetchall()

return render_template('instructors.html', instructors=instructors)

@app.route('/schedule')
def schedule():
cursor.execute("SELECT * FROM schedule")
schedule = cursor.fetchall()

return render_template('schedule.html', schedule=schedule)

@app.route('/contact')
def contact():
return render_template('contact.html')

@app.route('/success')
def success():
return render_template('success.html')

if __name__ == '__main__':
app.run(debug=True)


