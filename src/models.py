import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    subscriptionDate = Column(String(20))

    favorite_planets = relationship("FavoritePlanets")
    favorite_characters = relationship("FavoriteCharacters")


class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    total = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('planets.id'))

class FavoriteCahracters(Base):
    __tablename__ = 'favorite_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    total = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    orbitalPeriod = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    height = Column(Integer)
    mass = Column(Integer)
    hairColor = Column(String(20))
    skinColor = Column(String(20))
    eyeColor = Column(String(20))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
