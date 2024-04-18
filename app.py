from flask import Flask ,request
from flask_pymongo import PyMongo
from flask import render_template, redirect, url_for

app= Flask(__name__,static_url_path='/static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/Customer"
Mongo = PyMongo(app)
db = Mongo.db

@app.route('/', methods=['GET']) 
def index(): 
	## Display the HTML form template 
	return render_template('signup.html') 

@app.route ("/signup", methods=["POST", "GET"])
def signup():
  
    if request.method == "POST":

        # declare variables
        name=request.form["name"]
        surname=request.form["surname"]
        email=request.form["email"]
        password=request.form["password"]
    
    
        # adding user to the database
        user={"name":name, "surname":surname, "email":email, "password":password}
        db.user.insert_one(user)
             
        return render_template('login.html') 
    return 0    
        
@app.route ("/login", methods=["Post"])
def login():
    if request.method == "Post":
        # declare variables
        Email_Address=request.form["Email Address:"]
        password=request.form["password"]
       
     
        # adding user to the database
        user={" Email_Address": Email_Address, "password":password}
       
        db.user.find_one(user)
         
    return render_template("landing.html")

@app.route('/landing', methods=['GET']) 
def index(): 
	## Display the HTML form template 
	return render_template('landing.html')

# @app.route ("/login", methods=["Post"])
# def login():
#     if request.method == "Post":
#         # declare variables
#         name=request.form["name"]
#         time=request.form["time"]
#         action=request.form["action"]
       
     
#         # adding user to the database
#         user={" name":name, "time":time, "action":action}
       
#         db.user.find_one(user)
         
#     return render_template("landing.html")
        
if __name__ == "__main__":
    debug=True
    app.run()
 