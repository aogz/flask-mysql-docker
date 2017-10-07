# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from flask_login import current_user


@app.route('/')
def main():
    if current_user.is_authenticated:
        return render_template('main/profile.html')
    else:
        return render_template('main/landing.html')
