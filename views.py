from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('websiteContents.html')

@app.route("/submit", methods=["POST"])
def submit():
    date = request.form.get("birthday")
    return date

if __name__ == '__main__' :
    app.run(debug=True, port=8000)