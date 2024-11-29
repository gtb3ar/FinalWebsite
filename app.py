from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from website import create_app

# new instance of the Flask class

app = create_app()

if __name__=="__main__":
    app.run( debug = True )