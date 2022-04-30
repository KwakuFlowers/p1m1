import flask

app = flask.flask(__name__)


@app.route("/")
def main():
    return flask.render_template("main.html")


app.run()
