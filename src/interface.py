from tkinter import *
import webbrowser

def show_playlist(emotion, url):
    root = Tk()
    Label(root, text=f"Detected Emotion: {emotion}").pack()
    Button(root, text="Open Playlist", command=lambda: webbrowser.open(url)).pack()
    root.mainloop()