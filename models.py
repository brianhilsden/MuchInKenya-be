from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, bcrypt

class Customer(db.Model,SerializerMixin):
    __tablename__="customers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    phone_number = db.Column(db.String)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self,password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password_hash,password.encode("utf-8"))

    orders = db.relationship("Order",back_populates="customer",cascade="all,delete-orphan")
    reviews = db.relationship("Review",back_populates="customer",cascade="all,delete-orphan")

    serialize_rules = ("-orders.customer","-orders.driver","-orders","-reviews","-_password_hash")

    def __repr__(self):
        return f'<Customer id={self.id} name={self.name} email={self.email}>'

class Order(db.Model,SerializerMixin):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.id"))
    driver_id = db.Column(db.Integer,db.ForeignKey("drivers.id"))
    food_id = db.Column(db.Integer,db.ForeignKey("foods.id"))

    customer = db.relationship("Customer",back_populates="orders")
    driver = db.relationship("Driver",back_populates ="orders")
    food = db.relationship("Food", back_populates="orders")

   
    serialize_only=("driver.name","food.name","food.image","food.price")

    def __repr__(self):
        return f'<Order id={self.id} customer_id={self.customer_id} driver_id={self.driver_id} food_id={self.food_id}>'

class Driver(db.Model,SerializerMixin):
    __tablename__ = "drivers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    phone_number = db.Column(db.String)

    orders = db.relationship("Order",back_populates="driver")

    serialize_rules = ("-orders.driver",)

    def __repr__(self):
        return f'<Driver id={self.id} name={self.name}>'

class Restaurant(db.Model,SerializerMixin):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    image = db.Column(db.String)

    restaurant_foods = db.relationship("Restaurant_Food",back_populates="restaurant",cascade="all,delete-orphan")

    serialize_rules = ("-restaurant_foods.restaurant",)

    foods = association_proxy("restaurant_foods","food",creator=lambda food_obj:Restaurant_Food(food=food_obj))

    def __repr__(self):
        return f'<Restaurant id={self.id} name={self.name} location={self.location}>'

class Food(db.Model,SerializerMixin):
    __tablename__ = "foods"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)

    orders = db.relationship("Order", back_populates="food",cascade="all,delete-orphan")
    reviews = db.relationship("Review",back_populates="food",cascade="all,delete-orphan")
    restaurant_foods = db.relationship("Restaurant_Food",back_populates="food")

    serialize_rules = ("-restaurant_foods.food","-orders.food","-reviews.food")

    def __repr__(self):
        return f'<Food id={self.id} name={self.name} price={self.price}>'

class Restaurant_Food(db.Model,SerializerMixin):
    __tablename__ = "restaurant_foods"
    id = db.Column(db.Integer,primary_key=True)
    restaurant_id = db.Column(db.Integer,db.ForeignKey("restaurants.id"))
    food_id = db.Column(db.Integer,db.ForeignKey("foods.id"))

    restaurant = db.relationship("Restaurant",back_populates="restaurant_foods")
    food = db.relationship("Food",back_populates="restaurant_foods")

    serialize_rules = ("-restaurant.restaurant_foods","-food.restaurant_foods")

    def __repr__(self):
        return f'<Restaurant_Food id={self.id} restaurant_id={self.restaurant_id} food_id={self.food_id}>'

class Review(db.Model,SerializerMixin):
    __tablename__ = "reviews"
    id = db.Column(db.Integer,primary_key=True)
    message = db.Column(db.String)
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.id"))
    food_id = db.Column(db.Integer,db.ForeignKey("foods.id"))

    customer = db.relationship("Customer", back_populates = "reviews")
    food = db.relationship("Food",back_populates="reviews")

    serialize_rules=("-customer.reviews","-food.reviews")

    def __repr__(self):
        return f'<Review id={self.id} message={self.message}>'