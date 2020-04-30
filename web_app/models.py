from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

# create object SQLAlchemy and include instan the name of the istant flask object
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class Page(db.Model):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    tag = Column(String)
    contents = Column(String)
    url = Column(String)
    is_homepage = Column(Boolean)

# synchronize tables that don't yet exist in database. even though there is already a class
# db.create_all()
    def __repr__(self):
        return self.title

class Menu(db.Model):
    __tablename__= 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    order =  Column(Integer)

    page_id = Column(Integer, ForeignKey('page.id'))
    page = relationship('Page', backref=backref('Linked from Menu', uselist=False))

    def __repr__(self):
        return self.title