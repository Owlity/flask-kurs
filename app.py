
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/kurs")
def kurs():
 kursliste = ["fortnite", "valorant", "CS2", "Deadlock", "Highschool musical the musical the series extras"]
 return render_template("kurs.html", kursliste=kursliste)


if __name__ == "__main__":
    app.run(debug=True)

