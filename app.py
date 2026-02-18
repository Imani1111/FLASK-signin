#import flask 
from flask import * 

import pymysql 

#initialize the app 
app = Flask(__name__)


# 10 steps to create user signup 

#1.define your route/endpoint
@app.route("/api/signup", methods = ["POST"])

#2.define your function to signup 
def signup() :
    #3.get user inputs for the form 
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    phone = request.form["phone"]
    #4.establish connection to the database 
    connection = pymysql.connect(host="localhost" , user="root", password="", database="mbunisokogarden")

    #5.define your cursor 
    cursor = connection.cursor()
    #6.define sql insert
    sql = "insert into users(username, email, password, phone) values(%s , %s, %s, %s )"

    #7.define your data 
    data = (username , email , password , phone)

    #8.execute/run query
    cursor.execute(sql, data)

    #9.commit/save changes 
    connection.commit()

    #10.give responce to user
    return jsonify({"message" : "signup successful"})











#run application
app.run(debug = True)