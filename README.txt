After installing pipenv, do: pipenv shell.

Then do these four commands:
pipenv install flask
pipenv install psycopg2-binary
pipenv install flask-sqlalchemy
pipenv install gunicorn

IN CASE LOCKING FAILS:
then delete Pipfile.lock and retry the command you just did.


Then make to folders, static and templates
Keep your CSS in static.
Keep your three HTML files, login.html. mainpage.html and signUp.html in templates
You can copy the code from there if you like.

Then make a new file called app.py
then type these two lines of code:

    from flask import Flask, render_template, request
    from flask_sqlalchemy import SQLAlchemy

If you get some errors, do not worry. They are aviodable.
(On VSCode I got two errors saying that it could not be imported. Don't worry!)

Then type this: 
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

@app.route('/createaccount', methods=['POST'])
def createAccount():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        dateOfBirth = request.form['dateOfBirth']
        hobby = request.form['hobby']
        color = request.form['color']
        print(email, password, dateOfBirth, hobby, color)
        if email == '' or password ==  '' or  dateOfBirth =='' or hobby == '' or color == '':
            return render_template('signUp.html', message = 'Please fill out <u>all</u> fields!')
        return render_template('login.html', success = "You have succesfully made an account. Login to start the fun!")


if __name__ == '__main__':
    app.debug = True
    app.run()
