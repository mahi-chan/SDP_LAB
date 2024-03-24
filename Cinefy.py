import tkinter as tk
from Functions import VideoPlayer
# Invoke the VideoPlayer class from the Functions module

root = tk.Tk()
root.title("Cinefy")
player = VideoPlayer(root)
root.mainloop()