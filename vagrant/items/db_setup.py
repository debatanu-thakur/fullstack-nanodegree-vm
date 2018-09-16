import sys
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    def __init__(self, items = []):
        self._items = items

    __tablename__ = "catalog_category"
    name = Column ( String(80), nullable = False )
    id = Column( Integer, primary_key = True )
    image = Column( String(255), nullable = True )
    created_at = Column( DateTime, nullable=True, default=datetime.datetime.now )
    last_updated = Column( DateTime, nullable=True, default=datetime.datetime.now, onupdate=datetime.datetime.now )
    items=relationship("Item", order_by="Item.id", collection_class=ordering_list('id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'createdAt': self.created_at,
            'lastUpdated': self.last_updated,
            'items': [item.serialize for item in self.items]
        }

class Item(Base):
    __tablename__ = "catalog_items"
    
    id = Column( Integer, primary_key = True )
    title = Column( String(80), nullable = False )
    description = Column( String(255), nullable = False )
    image = Column( String(255), nullable = True )
    is_deleted = Column( Boolean, nullable=False, default=False )
    created_at = Column( DateTime, nullable=True, default=datetime.datetime.now )
    last_updated = Column( DateTime, nullable=True, default=datetime.datetime.now, onupdate=datetime.datetime.now )
    category_id = Column( Integer, ForeignKey("catalog_category.id") )
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image,
            'isDeleted': self.is_deleted,
            'createdAt': self.created_at,
            'lastUpdated': self.last_updated,
            'categoryId': self.category_id
        }


##### connect to db engine ######
engine = create_engine("sqlite:///catalog.db")
Base.metadata.create_all(engine)
