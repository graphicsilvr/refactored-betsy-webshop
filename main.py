__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from peewee import *
from models import User, Product, Tag, Transaction

def search(term):
    """
    Search for products by name or description.
    """
    print(f'Searching for products with term "{term}"...')
    # Use SQL's "LIKE" operator to search for products with matching name or description
    products = Product.select().where(
        (Product.name.contains(term, case=False)) | (Product.description.contains(term, case=False))
    )
    return products


def list_user_products(user_id):
    """
    List all products belonging to a specific user.
    """
    print(f'Listing products for user with ID {user_id}...')
    # Use a join to select all products belonging to the specified user
    products = Product.select().where(Product.user == user_id)
    return products


def list_products_per_tag(tag_id):
    """
    List all products with a specific tag.
    """
    print(f'Listing products for tag with ID {tag_id}...')
    # Use a join to select all products with the specified tag
    products = Product.select().join(Tag).where(Tag.id == tag_id)
    return products


def add_product_to_catalog(user_id, product):
    """
    Add a new product to the catalog, associated with a specific user.
    """
    user = User.get(User.id == user_id)
    product.user = user
    product.save()


def update_stock(product_id, new_quantity):
    """
    Update the quantity of a product in the catalog.
    """
    product = Product.get(Product.id == product_id)
    product.quantity = new_quantity
    product.save()


def purchase_product(product_id, buyer_id, quantity):
    """
    Purchase a specific quantity of a product.
    """
    product = Product.get(Product.id == product_id)
    buyer = User.get(User.id == buyer_id)
    transaction = Transaction.create(buyer=buyer, product=product, quantity=quantity)


def remove_product(product_id):
    """
    Remove a product from the catalog.
    """
    product = Product.get(Product.id == product_id)
    product.delete_instance()


def add_tag_to_product(product_id, tag_name):
    """
    Add a tag to a specific product.
    """
    product = Product.get(Product.id == product_id)
    tag, created = Tag.get_or_create(name=tag_name)
    product.tags.add(tag)
    product.save()


def remove_tag_from_product(product_id, tag_name):
    """
    Remove a tag from a specific product.
    """
    product = Product.get(Product.id == product_id)
    tag = Tag.get(Tag.name == tag_name)
    product.tags.remove(tag)
    product.save()


def update_tag(tag_id, new_name):
    """
    Update the name of a tag in the database.
    """
    tag = Tag.get(Tag.id == tag_id)
    tag.name = new_name
    tag.save()


def delete_tag(tag_id):
    """
    Delete a tag from the database.
    """
    tag = Tag.get(Tag.id == tag_id)
    tag.delete_instance()  
    
if __name__ == '__main__':
    db = SqliteDatabase('batabase.db')
    db.create_tables([User, Product, Tag, Transaction], safe=True)

    # Populate test data
def populate_test_database():
    user1 = User.create(
        name='John Doe',
        address='123 Main St, Anytown USA',
        billing_info='1234-5678-9012-3456'
    )

    user2 = User.create(
        name='Jane Doe',
        address='456 Market St, Anytown USA',
        billing_info='1234-5678-9012-6789'
    )

    tag1 = Tag.create(name='Clothing')
    tag2 = Tag.create(name='Home Decor')
    tag3 = Tag.create(name='Crafts')

    product1 = Product.create(
        name='Handmade Sweater',
        description='A cozy handmade sweater made from soft wool',
        price=50.0,
        quantity=20,
        user=user1
    )
    product1.tags.add(tag1)
    product1.tags.add(tag3)

    product2 = Product.create(
        name='Crochet Blanket',
        description='A handmade crochet blanket in a soft and warm acrylic yarn',
        price=70.0,
        quantity=15,
        user=user2
    )
    product2.tags.add(tag2)
    product2.tags.add(tag3)

    product3 = Product.create(
        name='Hand-Painted Mug',
        description='A unique hand-painted ceramic mug for your coffee or tea',
        price=15.0,
        quantity=25,
        user=user1
    )
    product3.tags.add(tag2)
    product3.tags.add(tag3)

    db.create_tables([User, Product, Tag, Transaction], safe=True)

    # Test search functionality
    term = 'sweater'
    print(f"Searching for '{term}'...")
    results = search(term)
    for product in results:
        print(f"{product.name}: {product.description}")
    print(f"Found {len(results)} results.")

    # Test list_user_products function
    user_id = 1
    products = list_user_products(user_id)
    for product in products:
        print(f"{product.name}: {product.description}")
    print(f"Found {len(products)} products for user with ID {user_id}.")

    # Test list_products_per_tag function
    tag_id = 2
    products = list_products_per_tag(tag_id)
    for product in products:
        print(f"{product.name}: {product.description}")
    print(f"Found {len(products)} products for tag with ID {tag_id}.")

    # Test add_product_to_catalog function
    user_id = 2
    new_product = Product(
        name="New product",
        description="This is a new product",
        price=10.00,
        quantity=5,
    )
    add_product_to_catalog(user_id, new_product)
    print(f"Added new product with ID {new_product.id} to user with ID {user_id}.")

    # Test update_stock function
    product_id = 1
    new_quantity = 20
    update_stock(product_id, new_quantity)
    print(f"Updated stock of product with ID {product_id} to {new_quantity}.")

    # Test purchase_product function
    product_id = 1
    buyer_id = 2
    quantity = 2
    purchase_product(product_id, buyer_id, quantity)
    print(f"Purchased {quantity} of product with ID {product_id} by user with ID {buyer_id}.")

    # Test remove_product function
    product_id = 2
    remove_product(product_id)
    print(f"Removed product with ID {product_id} from the catalog.")

    db.close()


