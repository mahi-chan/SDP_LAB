import tkinter as tk
from tkinter import filedialog
import vlc


class VideoPlayer:
    def _init_(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.vlc_instance = vlc.Instance()
        self.player = self.vlc_instance.media_player_new()
        self.media = None

        # widgets

        self.canvas = tk.Canvas(self.frame, width=640, height=480)
        self.load_button = tk.Button(self.frame, text="Load", command=self.load)
        self.play_button = tk.Button(self.frame, text="Play", command=self.play)
        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause)
        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop)
        self.volume_slider = tk.Scale(self.frame, from_=0, to=100, orient='horizontal', command=self.set_volume)
        self.speed_slider = tk.Scale(self.frame, from_=0.5, to=2, resolution=0.1, orient='horizontal', command=self.set_speed)


        # widget_packs

        self.canvas.pack()
        self.load_button.pack(side="bottom", padx=5, pady=5)
        self.play_button.pack(side='left', padx=5, pady=5)
        self.pause_button.pack(side='left', padx=5, pady=5)
        self.stop_button.pack(side='left', padx=5, pady=5)
        self.volume_slider.pack(side='right')
        self.speed_slider.pack(side='bottom')
        self.player.set_hwnd(self.canvas.winfo_id())
        
        