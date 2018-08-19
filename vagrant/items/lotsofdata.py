from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

cat=[]

cat1 = Category(name="Apparel", image="")
cat2 = Category(name="Kitchen", image="")
cat3 = Category(name="Swag", image="")
cat4 = Category(name="Office", image="")
cat5 = Category(name="Books", image="")
cat6 = Category(name="Stickers", image="")
cat7 = Category(name="Electronics", image="")
cat8 = Category(name="Umbrellas", image="")
cat = [
cat1,
cat2,
cat3,
cat4,
cat5,
cat6,
cat7,
cat8]
session.add_all(cat)
session.commit()


items = [Item(title="Gray Hooded Sweatshirt", description="Unless you live in a nudist colony, there are moments when the chill you feel demands that you put on something warm, and for those times, there's nothing better than this sharp MongoDB hoodie. Made of 100% cotton, this machine washable, mid-weight hoodie is all you need to stay comfortable when the temperature drops. And, since being able to keep your vital stuff with you is important, the hoodie features two roomy kangaroo pockets to ensure nothing you need ever gets lost.", image="/img/products/hoodie.jpg", category=cat1),
Item(title="Coffee Mug", description="A mug is a type of cup used for drinking hot beverages, such as coffee, tea, hot chocolate or soup. Mugs usually have handles, and hold a larger amount of fluid than other types of cup. Usually a mug holds approximately 12 US fluid ounces (350 ml) of liquid; double a tea cup. A mug is a less formal style of drink container and is not usually used in formal place settings, where a teacup or coffee cup is preferred.", image="/img/products/mug.jpg", category=cat2),
Item(title="Stress Ball", description="The moment life piles more onto your already heaping plate and you start feeling hopelessly overwhelmed, take a stress ball in hand and squeeze as hard as you can. Take a deep breath and just let that tension go. Repeat as needed. It will all be OK! Having something small, portable and close at hand is a must for stress management.", image="/img/products/stress-ball.jpg", category=cat3),
Item(title="Track Jacket", description="Crafted from ultra-soft combed cotton, this essential jacket features sporty contrast tipping and MongoDB's signature embroidered leaf.", image="/img/products/track-jacket.jpg", category=cat1),
Item(title="Women's T-shirt", description="Crafted from ultra-soft combed cotton, this essential t-shirt features sporty contrast tipping and MongoDB's signature leaf.", image="/img/products/white-mongo.jpg", category=cat1),
Item(title="Brown Carry-all Bag", description="Let your style speak for itself with this chic brown carry-all bag. Featuring a nylon exterior with solid contrast trim, brown in color, and MongoDB logo", image="/img/products/brown-bag.jpg", category=cat3),
Item(title="Brown Tumbler", description="The MongoDB Insulated Travel Tumbler is smartly designed to maintain temperatures and go anywhere. Dual wall construction will keep your beverages hot or cold for hours and a slide lock lid helps minimize spills.", image="/img/products/brown-tumbler.jpg", category=cat2),
Item(title="Pen (Green)", description="Erase and rewrite repeatedly without damaging documents. The needlepoint tip creates clear precise lines and the thermo-sensitive gel ink formula disappears with erasing friction.", image="/img/products/green-pen.jpg", category=cat4),
Item(title="Pen (Black)", description="Erase and rewrite repeatedly without damaging documents. The needlepoint tip creates clear precise lines and the thermo-sensitive gel ink formula disappears with erasing friction.", image="/img/products/pen.jpg", category=cat4),
Item(title="Green T-shirt", description="Crafted from ultra-soft combed cotton, this essential t-shirt features sporty contrast tipping and MongoDB's signature leaf.", image="/img/products/green-tshirt.jpg", category=cat1),
Item(title="MongoDB The Definitive Guide", description="Manage the huMONGOus amount of data collected through your web application with MongoDB. This authoritative introduction—written by a core contributor to the project—shows you the many advantages of using document-oriented databases, and demonstrates how this reliable, high-performance system allows for almost infinite horizontal scalability.", image="/img/products/guide-book.jpg", category=cat5),
Item(title="Leaf Sticker", description="Waterproof vinyl, will last 18 months outdoors.  Ideal for smooth flat surfaces like laptops, journals, windows etc.  Easy to remove.  50% discounts on all orders of any 6+", image="/img/products/leaf-sticker.jpg", category=cat6),
Item(title="USB Stick (Green)", description="MongoDB's Turbo USB 3.0 features lightning fast transfer speeds of up to 10X faster than standard MongoDB USB 2.0 drives. This ultra-fast USB allows for fast transfer of larger files such as movies and videos.", image="/img/products/greenusb.jpg", category=cat7),
Item(title="USB Stick (Leaf)", description="MongoDB's Turbo USB 3.0 features lightning fast transfer speeds of up to 10X faster than standard MongoDB USB 2.0 drives. This ultra-fast USB allows for fast transfer of larger files such as movies and videos.", image="/img/products/leaf-usb.jpg", category=cat7),
Item(title="Scaling MongoDB", description="Create a MongoDB cluster that will grow to meet the needs of your application. With this short and concise book, you'll get guidelines for setting up and using clusters to store a large volume of data, and learn how to access the data efficiently. In the process, you'll understand how to make your application work with a distributed database system.", image="/img/products/scaling-book.jpg", category=cat5),
Item(title="Powered by MongoDB Sticker", description="Waterproof vinyl, will last 18 months outdoors.  Ideal for smooth flat surfaces like laptops, journals, windows etc.  Easy to remove.  50% discounts on all orders of any 6+", image="/img/products/sticker.jpg", category=cat6),
Item(title="MongoDB Umbrella (Brown)", description="Our crook handle stick umbrella opens automatically with the push of a button. A traditional umbrella with classic appeal.", image="/img/products/umbrella-brown.jpg", category=cat8),
Item(title="MongoDB Umbrella (Gray)", description="Our crook handle stick umbrella opens automatically with the push of a button. A traditional umbrella with classic appeal.", image="/img/products/umbrella.jpg", category=cat8),
Item(title="MongoDB University Book", description="Keep the MongoDB commands you'll need at your fingertips with this concise book.", image="/img/products/univ-book.jpg", category=cat5),
Item(title="MongoDB University T-shirt", description="Crafted from ultra-soft combed cotton, this essential t-shirt features sporty contrast tipping and MongoDB's signature leaf.", image="/img/products/univ-tshirt.jpg", category=cat1),
Item(title="USB Stick", description="MongoDB's Turbo USB 3.0 features lightning fast transfer speeds of up to 10X faster than standard MongoDB USB 2.0 drives. This ultra-fast USB allows for fast transfer of larger files such as movies and videos.", image="/img/products/leaf-usb.jpg", category=cat7),
Item(title="Water Bottle", description="High quality glass bottle provides a healthier way to drink.  Silicone sleeve provides a good grip, a see-through window, and protects the glass vessel.  Eliminates toxic leaching that plastic can cause.  Innovative design holds 22-1/2 ounces.  Dishwasher safe", image="/img/products/water-bottle.jpg", category=cat2),
Item(title="WiredTiger T-shirt", description="Crafted from ultra-soft combed cotton, this essential t-shirt features sporty contrast tipping and MongoDB's signature leaf.", image="/img/products/wt-shirt.jpg", category=cat1)]

session.add_all(items)
session.commit()

print("added category items!")