
from config import Flask,request,make_response, app, api, Resource, db

from models import Customer, Order, Driver, Restaurant, Food, Restaurant_Food, Review



class Home(Resource):
    def get(self):
        return {"message":"Welcome to MuchInKenya"}

api.add_resource(Home,'/')

class Foods(Resource):
    def get (self):
        foods = []
        for food in Food.query.all():
            food_dict ={
                'id': food.id,
                'name': food.name,
                'description': food.description,
                'price': food.price,
            }
            foods.append(food_dict)
            reponse = make_response(
                foods,
                200
                )
        return reponse

    def post (self):
        if request.method == 'POST':
            try:
                    foods= Food(
                        name = request.get_json()["name"],
                        description= request.get_json()["description"],
                        price= request.get_json()["price"]
                    )
                    db.session.add(foods)
                    db.session.commit()
                    response= make_response(foods.to_dict(),201,{"content-type":"application/json"})
                    return response
            except ValueError as e:
                    message={"errors":["validation errors"]}
                    response= make_response(message,400)
                    return response

api.add_resource(Foods,'/foods')

class Restaurants(Resource):
    def get (self):
        restaurants = []
        for restaurant in Restaurant.query.all():
            restaurant_dict ={
                'id': restaurant.id,
                'name': restaurant.name,
                'location': restaurant.location,
            }
            restaurants.append(restaurant_dict)
            reponse = make_response(
                restaurants,
                200
                )
        return reponse

    def post(self):
         if request.method == 'POST':
            try:
                    restaurants= Restaurant(
                        name = request.get_json()["name"],
                        location= request.get_json()["location"],
                    )
                    db.session.add(restaurants)
                    db.session.commit()
                    response= make_response(restaurants.to_dict(),201,{"content-type":"application/json"})
                    return response
            except ValueError as e:
                    message={"errors":["validation errors"]}
                    response= make_response(message,400)
                    return response

api.add_resource(Restaurants,'/restaurant')

class Drivers(Resource):
    def get (self):
        drivers = []
        for driver in Driver.query.all():
            driver_dict ={
                'id': driver.id,
                'name': driver.name,
                'phone_number': driver.phone_number,
            }
            drivers.append(driver_dict)
            reponse = make_response(
                drivers,
                200
                )
        return reponse

    def post(self):
         if request.method == 'POST':
            try:
                    drivers= Driver(
                        name = request.get_json()["name"],
                        phone_number= request.get_json()["phone_number"],
                    )
                    db.session.add(drivers)
                    db.session.commit()
                    response= make_response(drivers.to_dict(),201,{"content-type":"application/json"})
                    return response
            except ValueError as e:
                    message={"errors":["validation errors"]}
                    response= make_response(message,400)
                    return response

api.add_resource(Drivers, '/drivers')

class Restaurant_foods(Resource):
    def get (self, id):
        restaurant = Restaurant.query.filter(Restaurant.id==id).first()
        if restaurant:
            restaurants_dict = {
                    'id': restaurant.id,
                    'name': restaurant.name,
                    'location': restaurant.location,
                    'restaurant_foods': [
                        {
                            'restaurant_id': food.restaurant_id,
                            'food_id': food.food_id,
                            'food': {
                                'id': food.food.id,
                                'name': food.food.name,
                                'description': food.food.description,
                                'price': food.food.price,
                            }
                        }
                        for food in restaurant.restaurant_foods
                    ]
                }
            response = make_response(restaurants_dict, 200)
            return response
             
api.add_resource(Restaurant_foods, '/restaurant_food/<int:id>')


class Orders(Resource):
    def get (self):
       pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

api.add_resource(Orders, '/orders')

class Customers(Resource):
    def get (self):
        customers = []
        for customer in Customer.query.all():
            customer_dict ={
                'id': customer.id,
                'name': customer.name,
                'email': customer.email,
                'phone_number': customer.phone_number,
            }
            customers.append(customer_dict)
            reponse = make_response(
                customers,
                200
                )
        return reponse


    def post(self):
         if request.method == 'POST':
            try:
                    customers= Customer(
                        name = request.get_json()["name"],
                        email= request.get_json()["email"],
                        phone_number= request.get_json()["phone_number"]
                    )
                    db.session.add(customers)
                    db.session.commit()
                    response= make_response(customers.to_dict(),201,{"content-type":"application/json"})
                    return response
            except ValueError as e:
                    message={"errors":["validation errors"]}
                    response= make_response(message,400)
                    return response

    def patch(self):
        pass

api.add_resource(Customers, '/customers')

class Reviews(Resource):
    def get (self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

api.add_resource(Reviews, '/reviews')




if __name__ == '__main__':
    app.run(port=5555,debug=True)

