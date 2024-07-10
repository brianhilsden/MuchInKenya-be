from config import Flask,request,make_response,app,db,api,Resource
from models import Customer,Order,Restaurant,Driver,Food,Restaurant_Food



#Add resources


if __name__ == "__main__":
    app.run(port=5555, debug=True)
