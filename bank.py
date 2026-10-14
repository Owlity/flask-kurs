# from flask import Flask, render_template, request


# app = Flask(__name__)

# @app.route("/")
# def index():
#     poeng = 16
#     return render_template("index.html", poeng=poeng)

# @app.route("/")
# def games():
#     gamelist = ["deadlock", "counterstrike", "spill", "fortnite", "etc"]
#     return render_template("index.html", gamelist=gamelist)


# if __name__ == "__main__":
#  app.run(debug=True)

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/registrering", methods=["GET", "POST"])
# def registrering():
#     if request.method == "POST":
#         navn = request.form["navn"]
#         epost = request.form["epost"]
#         alder = request.form["alder"]
#         kommentar = request.form["kommentar"]

#         return render_template(
#             "resultat.html",
#             navn=navn,
#             epost=epost,
#             alder=alder,
#             kommentar=kommentar
#         )

#     return render_template("registrering.html")


# if __name__ == "__main__":
#     app.run(debug=True)

@app.route("/kurs")
def kurs():
 kursliste = ["fortnite", "valorant", "CS2", "Deadlock", "Highschool musical the musical the series extras"]
 return render_template("kurs.html", kursliste=kursliste)