import tkinter as tk
from tkinter import filedialog
import vlc


class VideoPlayer:
    def __init__(self, master):
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
        self.subtitle_button = tk.Button(self.master, text="Load Subtitles", command=self.load_subtitles)

        # widget_packs

        self.canvas.pack()
        self.load_button.pack(side="bottom", padx=5, pady=5)
        self.play_button.pack(side='left', padx=5, pady=5)
        self.pause_button.pack(side='left', padx=5, pady=5)
        self.stop_button.pack(side='left', padx=5, pady=5)
        self.volume_slider.pack(side='right')
        self.speed_slider.pack(side='bottom')
        self.subtitle_button.pack(side='left', padx=5, pady=5)
        self.seek_var = tk.DoubleVar()
        self.seek_slider = tk.Scale(self.master, variable=self.seek_var, command=self.seek_video)
        self.seek_slider.pack(side='bottom')
        self.master.after(1000, self.update_seek_slider)
        self.player.set_hwnd(self.canvas.winfo_id())
        

# Methods of the features
    def load(self):
        filepath = filedialog.askopenfilename(filetypes=[("Video files", ".mp4;.avi;*.mkv")])
        self.media = self.vlc_instance.media_new(filepath)
        self.player.set_media(self.media)

    def play(self):
        self.player.play()
        self.update_seeker()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def set_volume(self, volume):
        self.player.audio_set_volume(int(volume))

    def set_speed(self, speed):
        self.player.set_rate(float(speed))

    def load_subtitles(self):
        subtitle_path = filedialog.askopenfilename(filetypes=[("Subtitle files", "*.srt")])
        if subtitle_path:
            self.player.video_set_subtitle_file(subtitle_path)

    def update_seek_slider(self):
        video_length = self.player.get_length() / 1000
        video_time = self.player.get_time() / 1000
        self.seek_var.set(video_time / video_length * 100)
        self.master.after(1000, self.update_seek_slider)

    def seek_video(self, value):
        video_length = self.player.get_length() / 1000
        seek_time = float(value) / 100 * video_length
        self.player.set_time(int(seek_time * 1000))


root = tk.Tk()
root.title("Cinefy")
player = VideoPlayer(root)
root.mainloop()
