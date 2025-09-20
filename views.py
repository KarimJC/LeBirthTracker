from flask import Flask, render_template, request, Blueprint
from datetime import datetime

app = Flask(__name__)

bp = Blueprint("home", __name__, url_prefix="/")

@app.route("/")
def home():
    return render_template('websiteContents.html')

@app.route("/submit", methods=["POST"])
def submit():
    date = request.form.get("birthday")
    return date

if __name__ == '__main__' :
    app.run(debug=True, port=8000)