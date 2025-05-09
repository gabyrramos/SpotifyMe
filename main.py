from src.emotionFile import detect_emotion
from src.spotify_auth import get_spotify_client, recommend_playlist
import webbrowser

def main():
    print("🎧Starting Emotion-Based Music Recommender...🎶")
    
    sp=get_spotify_client()
    emotion= detect_emotion()
    print(f"\nDetected emotion: {emotion}")
    
    if emotion:
        playlist_url=recommend_playlist(sp, emotion)
        print(f"\nOpening playlist: {playlist_url}")
        webbrowser.open(playlist_url)
        
if __name__ == "__main__":
    main()