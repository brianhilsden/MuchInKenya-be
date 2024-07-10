
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
    def get(self):
        orders_list = []
        for order in Order.query.all():
            order_dict = {
                "id": order.id,
                "food_name": order.food.name if order.food else None,
                "customer_name": order.customer.name if order.customer else None,
                "driver_name": order.driver.name if order.driver else None
            }
            orders_list.append(order_dict)
        return orders_list

    def post(self):
      if request.method == 'POST':
           try:
                orders = Order(
                     food_id = request.get_json()["food_id"],
                     customer_id = request.get_json()["customer_id"]
                )
                db.session.add(orders)
                db.session.commit()
                response = make_response(orders.to_dict(),201,{"content-type":"application/json"})
                return response
           except ValueError as e:
                message={"errors":["validation errors"]}
                response = make_response(message,400)
                return response

    def delete(self,order_id):
        order = Order.query.get(order_id)
        if not order:
             return {"message":"Order not found"}, 404
        
        db.session.delete(order)
        db.session.commit()

        return {"message":f"Order {order_id} deleted successfully"}, 200

api.add_resource(Orders, '/orders', '/orders/<int:order_id>')

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
         reviews_list = []
         for review in Review.query.all():
              review_dict = {
                   "id":review.id,
                   "message":review.message,
                   "customer":review.customer.name if review.customer else None,
                   "food":review.food.name if review.food else None
                }
              reviews_list.append(review_dict)
         return reviews_list

    def post(self):
        if request.method == 'POST':
             try:
                  review = Review(
                    message =  request.get_json()["message"],
                    customer_id = request.get_json()["customer_id"],
                    food_id = request.get_json()["food_id"]
                  )
                  db.session.add(review)
                  db.session.commit()
                  response = make_response(review.to_dict(),201,{"content-type":"application/json"})
                  return response
             except ValueError as e:
                  message={"errors":["validation errors"]}
                  response = make_response(message,400)
                  return response

    def delete(self,review_id):
        review = Review.query.get(review_id)
        if not review:
             return {"message":"Order not found"}, 404
        
        db.session.delete(review)
        db.session.commit()

        return {"message":f"Review {review_id} deleted successfully"}

api.add_resource(Reviews, '/reviews', '/reviews/<int:review_id>')




if __name__ == '__main__':
    app.run(port=5555,debug=True)

