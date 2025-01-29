from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/about")
def about():
    return send_from_directory(".", "about.html")

@app.route("/gallery")
def gallery():
    return send_from_directory(".", "gallery.html")

if __name__ == "__main__":
    app.run(debug=True)
