from tkinter import filedialog
import vlc
from gui import VideoPlayer
import os
import random


class VideoPlayer(VideoPlayer):
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
        seek_time = float(value) / 100 * video_length
        self.player.set_time(int(seek_time * 1000))

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
            self.set_aspect_ratio()
            self.set_media_and_play(media)
            if self.is_repeating:
                self.player.event_manager().event_attach(vlc.EventType.MediaPlayerEndReached, self.repeat_video)

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

    def repeat_video(self, event):
        if self.is_repeating:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_current_video()
