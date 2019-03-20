from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(Users)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name'         : self.name,
            'id'           : self.id,
        }


class MenuItem(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(Users)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name'         : self.name,
            'description'         : self.description,
            'id'         : self.id,
            'price'         : self.price,
            'course'         : self.course,
        }


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable  = False)
    email = Column(String(80), nullable = False)
    picture = Column(String(250))


engine = create_engine('sqlite:///restaurantmenuwithusers.db')


Base.metadata.create_all(engine)
