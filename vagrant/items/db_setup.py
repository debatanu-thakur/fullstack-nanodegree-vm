import sys
import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


Base = declarative_base()

class Category(Base):
    __tablename__ = "catalog_category"
    
    name = Column ( String(80), nullable = False )
    id = Column( Integer, primary_key = True )
    image = Column( String(255), nullable = True )
    created_at = Column( DateTime, nullable=True, default=datetime.datetime.now )
    last_updated = Column( DateTime, nullable=True, default=datetime.datetime.now, onupdate=datetime.datetime.now )

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


##### connect to db engine ######
engine = create_engine("sqlite:///catalog.db")
Base.metadata.create_all(engine)
