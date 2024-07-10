#!/usr/bin/env python3

from app import app
from models import db, Customer, Order, Driver, Restaurant, Food, Restaurant_Food

with app.app_context():

    # This will delete any existing rows so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Order.query.delete()
    Customer.query.delete()
    Driver.query.delete()
    Restaurant_Food.query.delete()
    Restaurant.query.delete()
    Food.query.delete()

    print("Creating customers...")
    customer1 = Customer(name="John Doe", email="john@example.com", phone_number=1234567890)
    customer2 = Customer(name="Jane Smith", email="jane@example.com", phone_number=2345678901)
    customers = [customer1, customer2]

    print("Creating drivers...")
    driver1 = Driver(name="Alice Johnson", phone_number=3456789012)
    driver2 = Driver(name="Bob Brown", phone_number=4567890123)
    drivers = [driver1, driver2]

    print("Creating restaurants...")
    restaurant1 = Restaurant(name="Pizza Palace", location="123 Main St")
    restaurant2 = Restaurant(name="Burger Barn", location="456 Elm St")
    restaurants = [restaurant1, restaurant2]

    print("Creating foods...")
    food1 = Food(name="Margherita Pizza", description="Classic cheese and tomato pizza", price=12)
    food2 = Food(name="Pepperoni Pizza", description="Spicy pepperoni with cheese", price=14)
    food3 = Food(name="Cheeseburger", description="Juicy beef patty with cheese", price=10)
    food4 = Food(name="Veggie Burger", description="Delicious vegetarian burger", price=9)
    foods = [food1, food2, food3, food4]

    print("Creating restaurant_foods...")
    rf1 = Restaurant_Food(restaurant=restaurant1, food=food1, special_instructions="Extra cheese")
    rf2 = Restaurant_Food(restaurant=restaurant1, food=food2, special_instructions="No onions")
    rf3 = Restaurant_Food(restaurant=restaurant2, food=food3, special_instructions="Extra pickles")
    rf4 = Restaurant_Food(restaurant=restaurant2, food=food4, special_instructions="Gluten-free bun")
    restaurant_foods = [rf1, rf2, rf3, rf4]

    print("Creating orders...")
    order1 = Order(customer=customer1, driver=driver1)
    order2 = Order(customer=customer2, driver=driver2)
    orders = [order1, order2]

    print("Adding data to the session...")
    db.session.add_all(customers)
    db.session.add_all(drivers)
    db.session.add_all(restaurants)
    db.session.add_all(foods)
    db.session.add_all(restaurant_foods)
    db.session.add_all(orders)
    db.session.commit()

    print("Seeding done!")
