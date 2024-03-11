import tkinter as tk
from tkinter import filedialog
import vlc
import os
import random

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
        self.show_playlist_button = tk.Button(root, text="Show Playlist", command=self.show_playlist)
        self.add_to_playlist_button = tk.Button(root, text="Add to Playlist", command=self.add_to_playlist)
        self.delete_from_playlist_button = tk.Button(root, text="Delete from Playlist",
                                                     command=self.delete_from_playlist)
        self.playlist = []
        self.current_index = 0
        self.is_shuffled = False
        self.is_repeating = False
        self.shuffle_button = tk.Button(root, text="Shuffle", command=self.shuffle_playlist)
        self.repeat_button = tk.Button(root, text="Repeat", command=self.toggle_repeat)
        self.aspect_ratio_label = tk.Label(self.frame, text="Aspect Ratio:")
        self.aspect_ratio_var = tk.StringVar()
        self.aspect_ratio_options = ["Original", "16:9", "4:3", "1:1"]
        self.aspect_ratio_menu = tk.OptionMenu(self.frame, self.aspect_ratio_var, *self.aspect_ratio_options)
        self.aspect_ratio_var.set("Original")


        # widget_packs

        self.canvas.pack()
        self.load_button.pack(side="bottom", padx=5, pady=5)
        self.play_button.pack(side='left', padx=5, pady=5)
        self.pause_button.pack(side='left', padx=5, pady=5)
        self.stop_button.pack(side='left', padx=5, pady=5)
        self.volume_slider.pack(side='right')
        self.speed_slider.pack(side='bottom')
        self.subtitle_button.pack(side='left', padx=5, pady=5)
        self.shuffle_button.pack()
        self.repeat_button.pack()
        self.show_playlist_button.pack()
        self.add_to_playlist_button.pack()
        self.delete_from_playlist_button.pack()
        self.aspect_ratio_label.pack(side='left', padx=5, pady=5)
        self.aspect_ratio_menu.pack(side='left', padx=5, pady=5)
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

        # Display the current playlist.

    def show_playlist(self):

        print("Playlist:")
        for i, video in enumerate(self.playlist):
            print(f"{i + 1}. {os.path.basename(video)}")

        # Add a video to the playlist.

    def add_to_playlist(self):

        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")])
        if file_path:
            self.playlist.append(file_path)
            print(f"{os.path.basename(file_path)} added to playlist.")

        # Delete a video from the playlist.

    def delete_from_playlist(self):

        if self.playlist:
            index_to_delete = int(input("Enter the index of the video to delete: ")) - 1
            if 0 <= index_to_delete < len(self.playlist):
                deleted_video = self.playlist.pop(index_to_delete)
                print(f"{os.path.basename(deleted_video)} removed from playlist.")
            else:
                print("Invalid index. Playlist unchanged.")

    def shuffle_playlist(self):
        if self.playlist:
            random.shuffle(self.playlist)
            self.is_shuffled = True
            self.current_index = 0
            self.play_current_video()

    def toggle_repeat(self):
        self.is_repeating = not self.is_repeating

    def play_current_video(self):
        if self.playlist:
            media = self.vlc_instance.media_new(self.playlist[self.current_index])
            aspect_ratio = self.aspect_ratio_var.get()
            if aspect_ratio == "16:9":
                self.player.video_set_aspect_ratio("16:9")
            elif aspect_ratio == "4:3":
                self.player.video_set_aspect_ratio("4:3")
            elif aspect_ratio == "1:1":
                self.player.video_set_aspect_ratio("1:1")
            else:
                self.player.video_set_aspect_ratio(None)

            self.player.set_media(media)
            self.player.play()

            if self.is_repeating:
                self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self.repeat_video)

    def repeat_video(self, event):
        if self.is_repeating:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_current_video()


root = tk.Tk()
root.title("Cinefy")
player = VideoPlayer(root)
root.mainloop()
