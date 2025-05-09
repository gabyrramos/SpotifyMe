import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    load_dotenv() #here we are loading variables: client id and client secret 
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://localhost:8080",
    scope="user-library-read"
))


def recommend_playlist(sp, emotion):
    emotion_to_playlist = {
        "happy": "Summer hits!",
        "sad": "Breakup songs",
        "angry": "Revenge Songs",
        "surprise": "Dance party",
        "neutral": "Chill hits",
        "fear": "Indie songs",
        "disgust": "Punk Rock"
    }
    
    #if emotion is not found then we are going to play a default playlist
    playlist_query = emotion_to_playlist.get(emotion, "Top Hits 2025")
    
    results = sp.search(q=playlist_query, type='playlist', limit=1)
    if results['playlists']['items']:
        return results['playlists']['items'][0]['external_urls']['spotify']
    else:
        return "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"