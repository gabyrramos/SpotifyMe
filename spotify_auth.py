import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv() #here we are loading variables: client id and client secret 

auth_manager = SpotifyClientCredentials(
    client_id=os.getenv("CLIENT_ID")
    client_secret=("CLIENT_SECRET")
    redirect_uri=("http://localhost:8080")
    scope="playlist-read-private"
)
sp = spotipy.Spotify(auth_manager=auth_manager)

