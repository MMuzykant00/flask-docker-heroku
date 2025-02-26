from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "aspartam_sugar"

@app.route("/")
def home():
    return "Welcome to my Flask app! Try <a href='/hello'>/hello</a> for a greeting."

@app.route("/hello")
def index():
    flash("What's your name?")  # ✅ Tutaj wysyłamy wiadomość flash
    return render_template("index.html")  # ✅ Flask powinien przekazać ją do szablonu

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!")  # ✅ Flash na ekranie powitania
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
