import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

def authenticate_spotify():
    """aqui vamos a autenticar a spotify usando los datos del .env """
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID")
        client_secret=("CLIENT_SECRET")
        redirect_uri=("http://localhost:8080")
        scope="playlist-read-private"
    ))
    return