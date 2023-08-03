from flask import render_template, Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("pages/index.html")


@app.route('/about')
def about():
    return render_template("pages/about.html")


@app.route("/api/hello-world")
def hello_world():
    return "Hello world!"


if __name__ == '__main__':
    app.run()