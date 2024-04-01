# test_video_player.py
import pytest
from unittest.mock import Mock
from Functions import VideoPlayer

def test_add_to_playlist(mock_video_player):
    # Mock the file dialog to return a video file path
    mock_video_player.add_to_playlist()
    # Verify that the video was added to the playlist
    assert len(mock_video_player.playlist) == 1



def test_set_volume(mock_video_player):
    # Test the set_volume method
    volume = 0.8  # Example volume value
    mock_video_player.set_volume(volume)
    # Add assertions to check if the volume was set correctly

if __name__ == "__main__":
    pytest.main()
