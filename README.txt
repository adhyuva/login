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