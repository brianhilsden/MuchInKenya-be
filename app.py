
from config import Flask,request,make_response,Migrate, Api, Resource, db

from models import Customer, Order, Driver, Restaurant, Food, Restaurant_Food


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://muchinkenya.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.json.compact = False

migrate = Migrate(app,db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        return {"message":"Welcome to MuchInKenya"}

app.add_resource(Home,'/')

class Foods(Resource):
    def get (self):
        pass

    def post (self):
        pass

app.add_resource(Foods,'/foods')

class Restaurant(Resource):
    def get (self):
        pass

    def post(self):
        pass

app.add_resource(Restaurant,'/restaurant')

class Drivers(Resource):
    def get (self):
        pass

    def post(self):
        pass

app.add_resource(Drivers, '/drivers')

class Restaurant_food(Resource):
    def get (self):
        pass

app.add_resource(Restaurant_food, '/restaurant_food')


class Orders(Resource):
    def get (self):
        pass

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

app.add_resource(Orders, '/orders')

class Customer(Resource):
    def get (self):
        pass

    def post(self):
        pass

    def patch(self):
        pass

app.add_resource(Customer, '/customers')

class Reviews(Resource):
    def get (self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

app.add_resource(Reviews, '/reviews')




if __name__ == '__main___':
    app.run(port=5555,debug=True)

