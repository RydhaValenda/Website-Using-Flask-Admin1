from web_app.app import create_app
from web_app.models import Page

app = create_app()

with app.app_context():
    page = Page()
    page.title = 'Homepage'
    page.is_homepage = True

    #objek db.session harus terikat pada suatu konteks apliksi flask yang berjalan
    db.session.add(page)
    db.session.commit()