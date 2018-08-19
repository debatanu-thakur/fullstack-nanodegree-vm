from flask import Flask, render_template
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from db_setup import Base, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = scoped_session(sessionmaker(bind=engine))



@app.route('/')
def DefaultLanding():
    session = DBSession()
    categories = session.query(Category)
    # output = render_template('restaurants.html', restaurants=restaurants)
    output = ""
    for cat in categories:
        output += cat.name
        output += "<br/>"
    remove_session()
    return output

@app.route('/restaurants/<int:restaurant_id>/')
def restaurants(restaurant_id):
    session = DBSession()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = render_template('menu.html', restaurant=restaurant, items=items)
    remove_session()
    return output

# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"

def remove_session():
    DBSession.remove()

if __name__=='__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)