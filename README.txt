Project created by following:
https://www.youtube.com/watch?v=Qr4QMBUPxWo

Project created in python, using flask (html, jinja)

Create database and insert data in python shell:
from market import db
db.create_all()
from market import Item
item1 = Item(name="IPhone 10", price=500, barcode='123456789012', description='desc')
db.session.add(item1)
db.session.commit()

Iteration in python shell:
for item in Item.query.all():
    item.name
