import flask
import random

from Spot import artistsongs

app = flask.flask(__name__)


@app.route("/")
def main():
    artistid = {
        "3TVXtAsR1Inumwj472S9r4",  # Drake
        "5f7VJjfbwm532GiveGC0ZK",  # Lil Baby
        "6vWDO969PvNqNYHIOW5v0m",  # Beyonce
        "2hlmm7s2ICUX0LVIhVFlZQ",  # Gunna
        "6l3HvQ5sa6mXTsMTB19rO5",  # J. cole
        "2YZyLoL8N0Wb9xBt1NhZWg",  # Kendrick Lamar
    }
    newartisitid = random.choice(artistid)
    (
        randsonginfo_name,
        randsonginfo_releasedate,
        randsonginfo_popularity,
        randsonginfo_extern,
        randsonginfo_imageurl,
        randsonginfo_imageH,
        randsonginfo_imageW,
    ) = artistsongs(newartisitid)

    return flask.render_template(
        "main.html",
        songname=randsonginfo_name,
        popularity=randsonginfo_popularity,
        spotlink=randsonginfo_extern,
        releasedate=randsonginfo_releasedate,
        imageurl=randsonginfo_imageurl,
        imageheight=randsonginfo_imageH,
        imagewidth=randsonginfo_imageW,
    )


app.run()
