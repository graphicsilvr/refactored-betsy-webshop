import datetime
import random


def populate_test_database():
    # connect to the database
    conn = sqlite3.connect('betsy.db')
    
    # create some example data
    users = [
        User(username='johndoe', password='password1', email='johndoe@example.com'),
        User(username='janedoe', password='password2', email='janedoe@example.com')
    ]
    
    products = [
        Product(name='product1', price=10.0),
        Product(name='product2', price=20.0)
    ]
    
    purchases = [
        Purchase(user_id=1, product_id=1, quantity=2),
        Purchase(user_id=2, product_id=2, quantity=1)
    ]
    
    # insert the data into the database
    with conn:
        for user in users:
            user.save(conn)
        
        for product in products:
            product.save(conn)
        
        for purchase in purchases:
            purchase.save(conn)
            
            
