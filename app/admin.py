from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security.core import current_user

from app import app, db
from app import models


class MyModelView(ModelView):
    def is_accessible(self):
        app.logger.debug('Auth admin : %s' % (current_user.roles))
        return current_user.is_authenticated and current_user.has_role('admin')


class UserView(MyModelView):
    pass


class RoleView(MyModelView):
    pass


admin = Admin(app, name='EpicVaultAdmin', template_mode='bootstrap3')

admin.add_view(UserView(models.User, db.session))
admin.add_view(RoleView(models.Role, db.session))
