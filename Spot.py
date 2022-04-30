from json import load
import os
from urllib import response
import requests
import json
import base64
import string
import random
import flask
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

GetReqURL = "https://api.spotify.com/v1"
api_token_url = "https://accounts.spotify.com/api/token"


def artistsongs(artid):
    Art_song_url = f"{GetReqURL}/artists/{artid}/top-tracks"
    country = {"country": "US"}

    head = {
        "Authorization": f"Bearer {authorize()}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    songs = requests.get(Art_song_url, params=country, headers=head)
    songinfo = songs.json()
    # songlist = songinfo["tracks"]
    print(songinfo)


def authorize():
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    DATA = {
        "Content-Type": "application/x-www-form-urlencoded",
        "grant_type": "client_credentials",
    }

    authkeydata = requests.post(
        api_token_url, auth=(CLIENT_ID, CLIENT_SECRET), data=DATA
    )
    reqkey = authkeydata.json()
    token = reqkey.get("access_token")
    # print(token)
    return f"{token}"


artistsongs("3TVXtAsR1Inumwj472S9r4")
