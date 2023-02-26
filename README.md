# Betsy Webshop
This is a project that requires you to master writing functions and function arguments, SQL joins, and database modelling. You will be designing a database for a fictional web marketplace called Betsy, where people can sell homemade goods. This assignment will test your skills in modelling data as well as using the peewee ORM.

# Modelling
The Betsy webshop database consists of the following models:

# User: contains name, address data, and billing information
Product: contains name, description, price per unit, and quantity describing the amount in stock
Tag: contains product tags, which are not duplicated
Transaction: links a buyer with a purchased product and a quantity of purchased items
Users can own multiple products, and only users can purchase goods.

# Querying
The following querying utilities are provided in main.py:

Search for products based on a term (case-insensitive)
View products of a given user
View all products for a given tag
Add a product to a user
Remove a product from a user
Update the stock quantity of a product
Handle a purchase between a buyer and a seller for a given product
Test Data
To test the functionality of the database and queries, you can use the populate_test_database() function to fill the database with example data. This function should be updated with example data that works with your queries.

# Extra search function
In the next phase of development, the search functionality of the betsy webshop will be optimized. The search should target both the name and description fields, and the products should be indexed so that the time spent on querying them is minimized. Additionally, the search should account for spelling mistakes made by users and return products even if a spelling error is present.