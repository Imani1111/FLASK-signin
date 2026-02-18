# import flask 
from flask import * 

# initialise the app 
app = Flask(__name__)

# define your route/endpoint 
@app.route("/api/home")
# define function 
def  home() :
    return jsonify({ "message" : "welcome home" })  

#products
@app.route("/api/products")
def products() :
    return jsonify({ "message" : "welcome to our products "})

#services 
@app.route("/api/services")
def services() :
    return jsonify({"message" : "welcome to our services"})

#contacts
@app.route("/api/contacts")
def contacts() :
    return jsonify({"message" : "welcome to our contact"})


#shopping
@app.route("/api/shopping")
def shopping() :
    return jsonify({"message" : "welcome to our shopping"})


#groceries
@app.route("/api/groceries")
def groceries() :
    return jsonify({"message" : "welcome to our groceries"})

#addition
@app.route("/api/addition" , methods = ["POST"])
def addition() :
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    answer = int(num1) + int(num2)
    return jsonify({"sum" : answer})


# subtraction 
@app.route("/api/subtraction" , methods = ["POST"])
def subtraction() :
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    answer = int(num1) - int(num2)
    return jsonify({"difference" : answer})

#multiplication 
@app.route("/api/multiplication" , methods = ["POST"])
def multiplication() :
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    answer = int(num1) * int(num2)
    return jsonify({"product" : answer})

#division 
@app.route("/api/division" , methods = ["POST"])
def division() :
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    answer = int(num1) / int(num2)
    return jsonify({"answer" : answer})    


#simple interest 
@app.route("/api/interest" , methods = ["POST"])
def interest() :
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    num3 = request.form["num3"]
    answer = (int(num1)*int(num2)*int(num3))/100
    return jsonify({"answer" : answer})  


# run the application 
app.run(debug=True)




