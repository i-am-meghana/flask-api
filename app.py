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

#path and query params
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

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
    
    



