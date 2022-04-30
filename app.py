import flask

from Spot import artistsongs

app = flask.flask(__name__)


@app.route("/")
def main():
    artistsongs() = (
        randsonginfo_name,
        randsonginfo_releasedate,
        randsonginfo_popularity,
        randsonginfo_extern,
        randsonginfo_imageurl,
        randsonginfo_imageH,
        randsonginfo_imageW,
    ) 
    return flask.render_template("main.html")
    

app.run()
