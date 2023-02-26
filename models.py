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

class Tag(BaseModel):
    name = CharField(max_length=100, unique=True, null=False)
    product = ForeignKeyField(Product, backref='tags')

class Transaction(BaseModel):
    buyer = ForeignKeyField(User, backref='transactions')
    product = ForeignKeyField(Product, backref='transactions')
    quantity = IntegerField(default=0, null=False)

    class Meta:
        database = db
        
