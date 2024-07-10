from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, bcrypt

class Customer(db.Model,SerializerMixin):
    __tablename__="customers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.Integer)

    orders = db.relationship("Order",back_populates="customer",cascade="all,delete-orphan")

    serialize_rules = ("-orders.customer",)

class Order(db.Model,SerializerMixin):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.id"))
    driver_id = db.Column(db.Integer,db.ForeignKey("drivers.id"))

    customer = db.relationship("Customer",back_populates="orders")
    driver = db.relationship("Driver",back_populates ="orders")
    serialize_rules = ("-customer.orders","-driver.orders")

class Driver(db.Model,SerializerMixin):
    __tablename__ = "drivers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    orders = db.relationship("Order",back_populates="driver")
    serialize_rules = ("-orders.driver",)

class Restaurant(db.Model,SerializerMixin):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    restaurant_foods = db.relationship("Restaurant_Food",back_populates="restaurant")
    serialize_rules = ("-restaurant_foods.restaurant",)

class Food(db.Model,SerializerMixin):
    __tablename__ = "foods"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)

    restaurant_foods = db.relationship("Restaurant_Food",back_populates="food")
    serialize_rules = ("-restaurant_foods.food",)

class Restaurant_Food(db.Model,SerializerMixin):
    __tablename__ = "restaurant_foods"
    id = db.Column(db.Integer,primary_key=True)
    restaurant_id = db.Column(db.Integer,db.ForeignKey("restaurants.id"))
    food_id = db.Column(db.Integer,db.ForeignKey("food.id"))
    special_instructions = db.Column(db.String)


