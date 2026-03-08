from flask import Flask, jsonify, request #Flask class


app = Flask(__name__) #object of Flask class


#basic route
@app.route("/")
def home():
    return "my first step (not really) into backend"


@app.route("/about")
def about():
    return "This is my about page"

#path param with path variable
@app.route("/user/<username>", methods = ["POST"])
def user(username):
    return jsonify({
        "message" : f"Got username {username}"
    })

#type casting in url params
@app.route("/api/user/<name>/<int:age>")
def user_details(name,age):
    user_data =  {
        "name" : name,
        "age" : age
    } 
    return jsonify(user_data)

#query params
@app.route("/api/search")
def search():
    age = request.args.get("age")
    return f"you are {age} years old"


@app.route("/api/user/<username>")
def user_profile(username):
    age = request.args.get("age") #typo in query key will return null 
    city = request.args.get("city")
    print(request.args)
    return jsonify({
        "name" : username,
        "age" : age,
        "city" : city
    })
    
    
@app.route("/api/create_user", methods = ["POST"])
def create_user():
    data = request.get_json() #method to get the json body 
    name = data.get("name")
    email = data.get("email")
    return jsonify({
        "name" : name,
        "email" : email,
        "message" :"User created!"
        
    })

#request.get_json   # the function object itself
#request.get_json() # calls the function and returns a dict


@app.route("/api/create_product", methods = ["POST"])
def product():
    data = request.get_json()
    print("Incoming request:", data)
    name = data["name"]
    price = data["price"] #wll throw key error if key not in client data returns 500
    brand = data.get("brand") #returns null if no such key in client data
    return jsonify({
        "name" : name,
        "price" : price,
        "brand" : brand,
        "message" : "Product created"
    })



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
    
    



