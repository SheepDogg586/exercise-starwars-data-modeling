import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites_character = relationship('Character', backref='user', uselist=False)
    favorites_planet = relationship('Planet', backref='user', uselist=False)

class Favorites(Base):
    __tablename__= "favorites"
    id = Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__= "planet"
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('favorites.id'))
    name = Column(String(250), nullable=False)

class Character(Base):
    __tablename__= "character"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('favorites.id'))
    name = Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__= "vehicle"
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('favorites.id'))
    name = Column(String(250), nullable=False)




# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
