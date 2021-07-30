from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        animal = request.form["animal"]
        session["user"] = user
        if not user:
            return render_template("home.html")
        return redirect(url_for("user"))
    else:
        return render_template("home.html")

@app.route("/fetch_data")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("home.html"))



if __name__ == '__main__':
    app.run(debug=True)
