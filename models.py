from peewee import *

db = SqliteDatabase('betsy.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField(max_length=100, unique=True, null=False)
    address = TextField(null=False)
    billing_info = TextField(null=False)

class Product(BaseModel):
    name = CharField(max_length=100, unique=True, null=False)
    description = TextField(null=False)
    price = DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = IntegerField(default=0, null=False)
    product_id = AutoField()

class Tag(BaseModel):
    name = CharField(max_length=100, unique=True, null=False)
    product = ForeignKeyField(Product, backref='tags')

class ProductTag(BaseModel):
    tag = ForeignKeyField(Tag, backref='products')
    product = ForeignKeyField(Product, backref='tags')

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions')
    product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField(default=0, null=False)

def create_database():
    db.connect()
    db.create_tables([User, Product, Tag, Transaction, ProductTag], safe=True)
    db.close()

def populate_test_database():
    # Create some users
    user1 = User.create(name='Alice', address='123 Main St', billing_info='Visa 1234-5678-9012-3456')
    user2 = User.create(name='Bob', address='456 Elm St', billing_info='Mastercard 9876-5432-1098-7654')

    # Create some products
    product1 = Product.create(name='Cloths', description='Fashionable clothes', price=39.99, quantity=10)
    product2 = Product.create(name='Shoes', description='Comfortable shoes', price=49.99, quantity=5)

    # Create some tags
    tag1 = Tag.create(name='tag1', product=product1)
    tag2 = Tag.create(name='tag2', product=product2)
    tag3 = Tag.create(name='tag3', product=product3)
    tag4 = Tag.create(name='tag4', product=product4)

    # Create some product tags
    product_tag1 = ProductTag.create(tag=tag1, product=product1)
    product_tag2 = ProductTag.create(tag=tag2, product=product2)
    product_tag3 = ProductTag.create(tag=tag3, product=product3)
    product_tag4 = ProductTag.create(tag=tag4, product=product4)

    # Create some transactions
    Transaction.create(buyer=user1, product=product1, quantity=2)
    Transaction.create(buyer=user2, product=product2, quantity=1)

if __name__ == '__main__':
    create_database()
    populate_test_database()
    print('Test database created and populated successfully.') 
