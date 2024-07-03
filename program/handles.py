from flask import Flask, render_template, request, redirect, url_for, jsonify
from user import database

dbclass = database()

app = Flask(__name__, template_folder='templates')
@app.route('/')
def hello_world():
    return render_template("index.html")

# Takes argument to ajax
@app.route('/ajax')
def ajax():
    return render_template("ajax.html")

#Handles ajax request 
@app.route("/process_ajax", methods=["POST", "GET"])
def process_ajax():
    if request.method == "POST":
        jsonData = request.get_json()
        name = jsonData["name"]
        password = jsonData["password"]
        response = database.UserExists(name, password)

        # user found
        if  response != 0:
            # return render_template("secure.html") 
            resp = jsonify(success = True)
            return resp
        else:
            return """0"""

    else:
        return """<h3>Method is GET</h3>"""

if __name__ == "__handles__":
    app.run(debug=True)