from config import db, app
from models import Customer, Order, Driver, Restaurant, Food, Restaurant_Food, Review

def seed_data():
    with app.app_context():
        # Clear existing data
        db.session.query(Review).delete()
        db.session.query(Order).delete()
        db.session.query(Restaurant_Food).delete()
        db.session.query(Food).delete()
        db.session.query(Restaurant).delete()
        db.session.query(Driver).delete()
        db.session.query(Customer).delete()
        db.session.commit()

        # Add Customers
        customers = [
            Customer(name="John Doe", email="john@example.com", phone_number="123456789"),
            Customer(name="Jane Doe", email="jane@example.com", phone_number="987654321")
        ]
        db.session.add_all(customers)

        # Add Drivers
        drivers = [
            Driver(name="Driver One", phone_number="555123456"),
            Driver(name="Driver Two", phone_number="555654321")
        ]
        db.session.add_all(drivers)

        # Add Restaurants
        restaurants = [
            Restaurant(name="Restaurant A", location="123 Main St"),
            Restaurant(name="Restaurant B", location="456 Elm St")
        ]
        db.session.add_all(restaurants)

        # Add Foods
        foods = [
            Food(name="Burger", description="A tasty burger", price=10),
            Food(name="Pizza", description="Delicious pizza", price=15)
        ]
        db.session.add_all(foods)

        # Add Restaurant_Foods
        restaurant_foods = [
            Restaurant_Food(restaurant=restaurants[0], food=foods[0]),
            Restaurant_Food(restaurant=restaurants[0], food=foods[1]),
            Restaurant_Food(restaurant=restaurants[1], food=foods[0]),
            Restaurant_Food(restaurant=restaurants[1], food=foods[1])
        ]
        db.session.add_all(restaurant_foods)

        # Add Orders
        orders = [
            Order(customer=customers[0], driver=drivers[0], food=foods[0]),
            Order(customer=customers[1], driver=drivers[1], food=foods[1])
        ]
        db.session.add_all(orders)

        # Add Reviews
        reviews = [
            Review(message="Great food!", customer=customers[0], food=foods[0]),
            Review(message="Excellent service!", customer=customers[1], food=foods[1])
        ]
        db.session.add_all(reviews)

        # Commit all changes
        db.session.commit()
        print("Database seeded with new data!")

if __name__ == "__main__":
    seed_data()