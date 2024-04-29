from tkinter import filedialog
from gui import VideoPlayer
import Playlist


class VideoPlayer(VideoPlayer, Playlist.Playlist):
    def __init__(self, root):
        super().__init__(root)

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

    def update_seek_slider(self):
        video_length = self.player.get_length() / 1000
        video_time = self.player.get_time() / 1000
        self.seek_var.set(video_time / video_length * 100)
        self.master.after(1000, self.update_seek_slider)

    def seek_video(self, value):
        video_length = self.player.get_length() / 1000
        seek_time = float(value) * video_length / 100
        self.player.set_time(int(seek_time * 1000))

    def set_aspect_ratio(self):
        aspect_ratio = self.aspect_ratio_var.get()
        if aspect_ratio == "16:9":
            self.player.video_set_aspect_ratio("16:9")
        elif aspect_ratio == "4:3":
            self.player.video_set_aspect_ratio("4:3")
        elif aspect_ratio == "1:1":
            self.player.video_set_aspect_ratio("1:1")
        else:
            self.player.video_set_aspect_ratio(None)

    def set_media_and_play(self, media):
        self.player.set_media(media)
        self.player.play()
