import tkinter as tk
from tkinter import filedialog
from tkvideo import tkvideo

root = tk.Tk()
root.title("Cinefy")

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
        
#2ndCommit

button_frame = tk.Frame(root)
button_frame.pack()


load_button = tk.Button(button_frame, text="Load", command=load_video)
load_button.grid(row=0, column=0, padx=10, pady=10)


pause_button = tk.Button(button_frame, text="Pause", command=pause_video)
pause_button.grid(row=0, column=1, padx=10, pady=10)


resume_button = tk.Button(button_frame, text="Resume", command=resume_video)
resume_button.grid(row=0, column=2, padx=10, pady=10)


stop_button = tk.Button(button_frame, text="Stop", command=stop_video)
stop_button.grid(row=0, column=3, padx=10, pady=10)

root.mainloop()        