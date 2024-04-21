# test_video_player.py
import pytest
from unittest.mock import MagicMock
from Functions import VideoPlayer
import tkinter as tk
from unittest.mock import Mock, patch


@pytest.fixture
def mock_video_player():
    master = tk.Tk()
    player = VideoPlayer(master)
    player.player = MagicMock()
    player.vlc_instance = MagicMock()
    player.media = MagicMock()
    return player


def test_load(mock_video_player):
    with patch('tkinter.filedialog.askopenfilename', return_value='test.mp4'), \
            patch('vlc.Instance.media_new') as mock_media_new:
        mock_video_player.vlc_instance.media_new = mock_media_new
        mock_video_player.load()
        mock_media_new.assert_called_once_with('test.mp4')


def test_add_to_playlist(mock_video_player):
    mock_video_player.add_to_playlist()
    assert len(mock_video_player.playlist) == 1


def test_set_volume(mock_video_player):
    volume = 50
    mock_video_player.set_volume(volume)
    mock_video_player.player.audio_set_volume.assert_called_once_with(int(volume))


def test_set_speed(mock_video_player):
    speed = 1.5
    mock_video_player.set_speed(speed)
    mock_video_player.player.set_rate.assert_called_once_with(float(speed))


def test_play(mock_video_player):
    mock_video_player.update_seeker = MagicMock()
    mock_video_player.play()
    mock_video_player.player.play.assert_called_once()
    mock_video_player.update_seeker.assert_called_once()


def test_pause(mock_video_player):
    mock_video_player.pause()
    mock_video_player.player.pause.assert_called_once()


def test_stop(mock_video_player):
    mock_video_player.stop()
    mock_video_player.player.stop.assert_called_once()


def test_seek_video(mock_video_player):
    value = 50
    mock_video_player.player.get_length.return_value = 5000
    mock_video_player.seek_video(value)
    mock_video_player.player.set_time.assert_called_once_with(2500)


if __name__ == "__main__":
    pytest.main()
