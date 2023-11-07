from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def main_page():
    return render_template('/welcome.html')