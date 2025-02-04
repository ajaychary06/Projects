from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    program_name = db.Column(db.String(100), nullable=False)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    students = Student.query.all()
    universities = University.query.all()
    return render_template('index.html', students=students, universities=universities)

# Student CRUD operations

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    course_id = request.form['course_id']
    new_student = Student(name=name, course_id=course_id)
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.course_id = request.form['course_id']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student)

@app.route('/delete_student/<int:id>')
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

# University CRUD operations

@app.route('/add_university', methods=['POST'])
def add_university():
    name = request.form['name']
    program_name = request.form['program_name']
    new_university = University(name=name, program_name=program_name)
    db.session.add(new_university)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit_university/<int:id>', methods=['GET', 'POST'])
def edit_university(id):
    university = University.query.get(id)
    if request.method == 'POST':
        university.name = request.form['name']
        university.program_name = request.form['program_name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_university.html', university=university)

@app.route('/delete_university/<int:id>')
def delete_university(id):
    university = University.query.get(id)
    db.session.delete(university)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
