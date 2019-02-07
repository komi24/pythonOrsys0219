from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/home")
def home():
	return "Home"

@app.route("/form", methods=["POST"])
def form():
	print("FORM")
	print(request.form.get("firstname"))
	print(request.form.get("lastname"))
	return "Home"

app.run(port=3000, debug=True)