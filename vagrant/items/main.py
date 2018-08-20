from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from db_setup import Base, Category, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = scoped_session(sessionmaker(bind=engine))



@app.route('/')
@app.route('/catalog/')
def DefaultLanding():
    session = DBSession()
    categories = session.query(Category)
    for cat in categories:
        items = session.query(Item).filter_by(category_id = cat.id)
        cat.items = items
    output = render_template('home.html', categories=categories)
    remove_session()
    return output


@app.route('/catalog/<string:category_name>/')
def catalog(category_name):
    session = DBSession()
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category_id = category.id, is_deleted=False)
    output = render_template('category.html', category=category, items=items)
    remove_session()
    return output

@app.route('/catalog/<string:category_name>/add/', methods=['GET', 'POST'])
def addItem(category_name):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image = ''
        session = DBSession()
        category = session.query(Category).filter_by(name=category_name).one()
        item = Item(title=title, description=description, image=image, category_id=category.id)
        session.add(item)
        session.commit()
        remove_session()
        return redirect(url_for('catalog',category_name=category_name))
    else:
        session = DBSession()
        category = session.query(Category).filter_by(name=category_name).one()
        output = render_template('add.html', category=category )
        remove_session()
    return output
# Task 2: Create route for editMenuItem function here

@app.route('/catalog/<string:category_name>/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(category_name, item_id):
    session = DBSession()
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(id=item_id, category_id=category.id).one()
    if request.method == 'POST':
        item.title = request.form['title']
        item.description = request.form['description']
        session.add(item)
        session.commit()
        remove_session()
        return redirect(url_for('catalog', category_name=category_name))
    else:
        output = render_template('edit.html', category=category, item=item )
        remove_session()
    return output

# Task 3: Create a route for deleteMenuItem function here

@app.route('/catalog/<string:category_name>/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(category_name, item_id):
    session = DBSession()
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        item.is_deleted=True
        session.add(item)
        session.commit()
        remove_session()
        return redirect(url_for('catalog', category_name=category_name))
    else:
        output = render_template('delete.html', category=category, item=item)
        remove_session()
    return output


@app.route('/json/catalog/')
def JSONDefault():
    session = DBSession()
    categories = session.query(Category)
    for cat in categories:
        items = session.query(Item).filter_by(category_id = cat.id)
    remove_session()
    output = jsonify(Categories=[cat.serialize for cat in categories])
    return output

@app.route('/json/catalog/all/')
def JSONDefaultAll():
    session = DBSession()
    categories = session.query(Category)
    all_data = []
    for cat in categories:
        items=session.query(Item).filter_by(category_id = cat.id)
        cat.items.extend(items)
    remove_session()
    output = jsonify(Categories=[cat.serialize for cat in categories])
    return output

@app.route('/json/catalog/<int:category_id>/')
def JSONCatalog(category_id):
    session = DBSession()
    items = session.query(Item).filter_by(category_id=category_id)
    remove_session()
    output = jsonify(Items=[item.serialize for item in items])
    return output

@app.route('/json/catalog/<int:category_id>/<int:item_id>/')
def JSONItem(category_id, item_id):
    session = DBSession()
    item = session.query(Item).filter_by(id=item_id).one()
    remove_session()
    output = jsonify(Item=item.serialize)
    return output


def remove_session():
    DBSession.remove()

if __name__=='__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)