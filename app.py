from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def index():
    return render_template("index.html")

@app.route("/contact")
def index():
    return render_template("index.html")

# portraits, dance, auditions, interior design
@app.route("/portfolio")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)