from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('result.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        marks = request.form['marks']
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO students (name, marks) VALUES (?, ?)", (name, marks))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db()
    cur = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        marks = request.form['marks']
        cur.execute("UPDATE students SET name=?, marks=? WHERE id=?", (name, marks, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cur.fetchone()
    conn.close()
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
