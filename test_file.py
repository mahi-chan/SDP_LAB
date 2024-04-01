# test_video_player.py
import pytest
from unittest.mock import MagicMock
from Functions import VideoPlayer
import tkinter as tk  # Import tkinter for creating a master instance

@pytest.fixture
def mock_video_player():
    # Create a mock VideoPlayer instance with a valid master (tk.Tk()) instance
    master = tk.Tk()  # Create a master instance
    player = VideoPlayer(master)  # Pass the master instance to VideoPlayer
    player.get_length = MagicMock(return_value=10000)  # Mock get_length
    player.set_time = MagicMock()  # Mock set_time
    return player


def test_load(mock_video_player):
    # Test the load method
    # You can mock the file dialog or provide a sample file path
    # and assert that the media is set correctly
    filepath = "sample_video.mkv"
    mock_video_player.load()
    actual_mrl = mock_video_player.media.get_mrl()
    actual_filename = actual_mrl.split("/")[-1]  # Get the filename part
    assert actual_filename == filepath


def test_add_to_playlist(mock_video_player):
    # Mock the file dialog to return a video file path
    mock_video_player.add_to_playlist()
    # Verify that the video was added to the playlist
    assert len(mock_video_player.playlist) == 1

def test_set_speed(mock_video_player):
    # Test the set_speed method
    speed = 2  # Example speed value
    mock_video_player.set_speed(speed)

def test_set_volume(mock_video_player):
    # Test the set_volume method
    volume = 0.8  # Example volume value
    mock_video_player.set_volume(volume)
    # Add assertions to check if the volume was set correctly

if __name__ == "__main__":
    pytest.main()
