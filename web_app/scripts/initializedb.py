# from web_app.app import create_app
# from web_app.models import Page

# add to sys path python with take now directory and then add directory web_app
import sys,os
sys.path.append(os.getcwd() + '/web_app') #a ccording mark directory as sources

from app import create_app
from models import Page, db, Role, User

app = create_app()

with app.app_context():
    # to add user as admin
    admin_role = Role()
    admin_role.name = 'admin'
    db.session.add(admin_role)
    db.session.commit()

    root = User()
    root.email = 'ryval.study@gmail.com'
    root.password = '123456'
    root.active = True
    root.roles.append(admin_role)
    db.session.add(root)

    page = Page()
    page.title = 'Homepage'
    page.contents = "<h1>Welcome to my website</h1>"
    page.is_homepage = True

    #objek db.session harus terikat pada suatu konteks apliksi flask yang berjalan
    db.session.add(page)
    db.session.commit()