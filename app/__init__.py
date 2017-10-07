# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from flask_mail import Mail

from app import config

app = Flask(__name__)
app.config.from_object(config)

app.add_template_global(current_user, 'current_user')

mail = Mail(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

from app import views
from app import models
from app import security
from app import admin
