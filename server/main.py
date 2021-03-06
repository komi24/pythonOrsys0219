from flask import Flask, render_template, request, redirect
from models import orm
from models.Personne import Personne


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orsys0219.sqlite3"

with app.app_context():
	orm.init_app(app)
	orm.create_all()


@app.route("/")
def hello():
	liste_personnes = Personne.query.all()
	return render_template("index.html", liste=liste_personnes)

@app.route("/home")
def home():
	return "Home"

@app.route("/edit/<id>", methods=["POST"])
def edit(id):
	Personne.query.filter_by(id=id).update({
		"firstname": request.form.get("firstname"),
		"lastname": request.form.get("lastname")})
	orm.session.commit()
	return redirect("/")

@app.route("/personne/<id>")
def profile(id):
	ma_personne = Personne.query.get(id)
	return render_template("profile.html", personne=ma_personne)

@app.route("/form", methods=["POST"])
def form():
	print("FORM")
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")

	une_personne = Personne(firstname, lastname, 20)
	orm.session.add(une_personne)
	orm.session.commit()

	return redirect("/")

app.run(port=3000, debug=True)