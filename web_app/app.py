from flask import Flask, render_template

from web_app.models import db, Page


def create_app():
    app = Flask(__name__)
    # konfigurasi debug dibawah berfungsi flask mengambil perubahan2 dalam html
    # app.config['DEBUG'] = True

    # file config diambil dari file mode py
    app.config.from_pyfile('settings.py')

    db.init_app(app)
    # "route" alamat url yang akan ditangani oleh app ini
    @app.route('/') #decorator(akan memastikan fungsi index akan bisa dipanggil oleh flask)
    def index():
        # connect to database use sqlalchemy
        page = Page.query.filter_by(id=1).first()
        contents = 'empty'
        if page is not None:
            contents = page.contents

        return render_template('index.html', TITLE='Flask-01', CONTENT=contents)

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


    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Flask-01')

    @app.route('/testdb')
    def testdb():
    # connect ke database table
        import psycopg2

    # important "host", here run not in "localhost"
    # but, this use docker, host run according by name service
        con = psycopg2.connect('dbname=flask01 user=devuser password=devpassword host=postgres')
    # use object cursor , can be execute syntax database
        cur = con.cursor()

        cur.execute('select * from page;')

    # cur.fetchone() produce data like the column
        id, title = cur.fetchone()
        con.close()
        return 'output table page: {} - {}'. format(id, title)

    return app

# # IP "0.0.0.0" bisa dites diinternal network
# app.run('0.0.0.0', debug=True)