from flask import Flask, jsonify #Flask class


app = Flask(__name__) #object of Flask class

@app.route("/")
def home():
    return "my first step (not really) into backend"

@app.route("/about")
def about():
    return "This is my about page"

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/age/<int:age>")
def age_of(age):
    return f"you are {age}'s old"

@app.route("/api/user/<name>/<int:age>")
def user_details(name,age):
    user_data =  {
        "name" : name,
        "age" : age
    } 
    return jsonify(user_data)


if __name__ == "__main__":
    app.run(debug=True)