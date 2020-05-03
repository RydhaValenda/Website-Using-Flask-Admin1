from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required
from flask_security import SQLAlchemyUserDatastore, Security
from models import db, Page, Menu, User, Role
from views import PageModelView, MenuModelView, SecureAdminIndexView


def create_app():
    app = Flask(__name__)
    # konfigurasi debug dibawah berfungsi flask mengambil perubahan2 dalam html
    # app.config['DEBUG'] = True

    # file config diambil dari file mode py
    app.config.from_pyfile('settings.py')

    db.init_app(app)

    admin = Admin(app, name='Flask-01', template_mode='bootstrap3', index_view=SecureAdminIndexView())
    admin.add_view(PageModelView(Page, db.session))
    admin.add_view(MenuModelView(Menu, db.session))

    # we tell to flask security that there will be a connection from the admin flask to this app via sqlalchemy
    user_datastore =  SQLAlchemyUserDatastore(db,  User, Role)
    security = Security(app, user_datastore)

    # "route" alamat url yang akan ditangani oleh app ini
    @app.route('/') #decorator(akan memastikan fungsi index akan bisa dipanggil oleh flask)
    @app.route('/<url>') #index defined handles without arguments and with argument
    def index(url=None):
        print('here',url)
        if url is not None:
            # ex /about
            page = Page.query.filter_by(url=url).first()             # connect to database use sqlalchemy
        else:
            # ex /
            page = Page.query.filter_by(is_homepage=True).first()

        if page is None:
            # TODO cute 404
            return 'Page not found for {} or homepage not set'.format(url)

        contents = 'empty'
        if page is not None:
            contents = page.contents
        menu = Menu.query.order_by('order')

        return render_template('index.html', TITLE='Flask-01', CONTENT=contents, menu=menu)

        # @app.route('/rahasia')
        # create decorator (penanda suatu fungsi)
    @app.route('/rahasia')
    @login_required
    def rahasia():
        return '<h1>Luke dies!</h1>'

    return app
        # # connect ke database table
        # import psycopg2
        #
        # # important "host", here run not in "localhost"
        # # but, this use docker, host run according by name service
        # con = psycopg2.connect('dbname=flask01 user=devuser password=devpassword host=postgres')
        # # use object cursor , can be execute syntax database
        # cur = con.cursor()
        #
        # cur.execute('select contents from page where id = 1')
        #
        # # cur.fetchone() produce data like the column
        # contents = cur.fetchone() # restore tuple. (0,1,2)
        # con.close()
        # return render_template('index.html', TITLE='Flask-01', CONTENT=contents[0])

    #  THIS RUN STATIC
    # @app.route('/about')
    # def about():
    #     return render_template('about.html', TITLE='Flask-01')

    # @app.route('/testdb')
    # def testdb():
    # # connect ke database table
    #     import psycopg2
    #
    # # important "host", here run not in "localhost"
    # # but, this use docker, host run according by name service
    #     con = psycopg2.connect('dbname=flask01 user=devuser password=devpassword host=postgres')
    # # use object cursor , can be execute syntax database
    #     cur = con.cursor()
    #
    #     cur.execute('select * from page;')
    #
    # # cur.fetchone() produce data like the column
    #     id, title = cur.fetchone()
    #     con.close()
    #     return 'output table page: {} - {}'. format(id, title)



# # IP "0.0.0.0" bisa dites diinternal network
# app.run('0.0.0.0', debug=True)