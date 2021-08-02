from flask import Flask, render_template, request, url_for, redirect, session
import json
app = Flask(__name__)
app.secret_key = "hello"

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]



        session["user"] = user
        if not user:
            return render_template("home.html")
        return redirect(url_for("user"))
    else:
        return render_template("home.html")

@app.route("/fetch_data",  methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        animal = "foxes"


        with open('pictures.json') as f:
            data = json.load(f)

            for animal in data['dogs']:
                name = (animal)['name']
                image = (animal['image'])

        return render_template("fetch.html", names = name, image = image)
    else:
        return redirect(url_for("home.html"))


