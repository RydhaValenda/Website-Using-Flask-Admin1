from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

# create object SQLAlchemy and include instan the name of the istant flask object
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class Page(db.Model):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    tag = Column(String)
    contents = Column(String)


# synchronize tables that don't yet exist in database. even though there is already a class
# db.create_all()

class Menu(db.Model):
    __tablename__= 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    order =  Column(Integer)

    page_id = Column(Integer, ForeignKey('page.id'))
    page = relationship('Page', backref=backref('Linked from Menu'))