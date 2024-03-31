from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "you are welcome"

@app.route("/create")
def create():
    address="4 oladimaji,lagos"
    phone="09134343535"
    return "This are my details " + address + "," + phone 
 
 
 
 if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5001, debug =True)