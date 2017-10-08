# -*- coding: utf-8 -*-
from app import app
from flask import render_template, redirect
from flask_login import current_user


@app.route('/')
def main():
    if current_user.is_authenticated:
        return redirect('/profile')
    else:
        return render_template('main/landing.html')


@app.route('/settings')
def settings():
    return render_template('main/settings.html')


@app.route('/profile')
def profile():
    return render_template('main/profile.html')
