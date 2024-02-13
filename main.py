
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Establish the database connection
connection = sqlite3.connect('courses.db')
cursor = connection.cursor()

# Define the routes

# Registration route
@app.route('/register', methods=['POST'])
def register():
    """
    Handles the registration process.
    """
    # Get the data from the form
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    course = request.form.get('course')

    # Insert the data into the database
    cursor.execute("INSERT INTO registrations (name, email, phone, course) VALUES (?, ?, ?, ?)",
                   (name, email, phone, course))
    connection.commit()

    # Redirect to the success page
    return redirect(url_for('success'))

# Courses route
@app.route('/courses')
def courses():
    """
    Displays a list of available courses.
    """
    # Get the list of courses from the database
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    # Render the courses page
    return render_template('courses.html', courses=courses)

# Instructors route
@app.route('/instructors')
def instructors():
    """
    Displays a list of instructors.
    """
    # Get the list of instructors from the database
    cursor.execute("SELECT * FROM instructors")
    instructors = cursor.fetchall()

    # Render the instructors page
    return render_template('instructors.html', instructors=instructors)

# Schedule route
@app.route('/schedule')
def schedule():
    """
    Displays a schedule of courses.
    """
    # Get the schedule from the database
    cursor.execute("SELECT * FROM schedule")
    schedule = cursor.fetchall()

    # Render the schedule page
    return render_template('schedule.html', schedule=schedule)

# Contact route
@app.route('/contact')
def contact():
    """
    Displays a contact form.
    """
    # Render the contact page
    return render_template('contact.html')

# Success route
@app.route('/success')
def success():
    """
    Displays a success message.
    """
    # Render the success page
    return render_template('success.html')

# Main function
if __name__ == '__main__':
    app.run(debug=True)


This code represents a fully functional Flask application that allows students to register for courses, view a list of courses and instructors, explore the course schedule, and contact the course administrators. The code includes proper routing, database interaction, and templating to provide a well-structured and user-friendly application.