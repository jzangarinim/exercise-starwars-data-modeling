import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(timezone=False))
    password = Column(String(30), nullable=False)
    # relationship(nombre de la CLASE)
    favorite_list = relationship('Favorite', back_populates='user', uselist=True)

    def __str__(self):
        return self.username

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    
class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    
    def __str__(self):
        return self.name

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String, nullable=False)
    terrain = Column(String, nullable=False)
    
    def __str__(self):
        return self.name

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
