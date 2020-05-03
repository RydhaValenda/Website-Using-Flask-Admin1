# konfigurasi debug dibawah berfungsi flask mengambil perubahan2 dalam html
DEBUG = True

# Connect SQLALCHEMY to database only setting.py
SQLALCHEMY_DATABASE_URI = 'postgresql://devuser:devpassword@postgres:5432/flask01'

# if turned on it will track changes in the table, but will reduce performance
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configure to identify the form and identify data sent by the post
SECRET_KEY = 'halohaybos'

# an initial data used by an algorithm to create randomness
SECURITY_PASSWORD_SALT = 'bektuwesandihaybos'