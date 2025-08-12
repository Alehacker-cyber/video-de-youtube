from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<filename>")
def serve_audio(filename):
    return send_from_directory(".", filename)
