import tkinter as tk
from tkinter import filedialog
from tkvideo import tkvideo
root = tk.Tk()
root.title("Video Player")
video_label = tk.Label(root)
video_label.pack()
player = None
def load_video():
    global player
    file_path = filedialog.askopenfilename(filetypes=[("Video files", ".mp4;.avi;*.mkv")])
    if file_path:
        player = tkvideo(file_path, video_label, loop=0)
        player.play()
def pause_video():
    global player 
    if player: 
        player.pause()
def resume_video():
    global player 
    if player: 
        player.resume()
def stop_video():
    global player 
    if player: 
        player.stop()
        player = None