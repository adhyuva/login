from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signUp.html')

@app.route('/mainpage', methods=['POST'])
def login():
    return render_template('mainpage.html')

@app.route('/createAccount', methods=['POST'])
def createAccount():
    email = request.form['email']
    password = request.form['password']
    dateOfBirth = request.form['dateOfBirth']
    hobby = request.form['hobby']
    color = request.form['color']
    print(email, password, dateOfBirth, hobby, color)
    if email == '' or password ==  '' or  dateOfBirth =='' or hobby == '' or color == '':
        return render_template('signUp.html', message = 'Uh - oh! Make sure to fill all the required fields')
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
