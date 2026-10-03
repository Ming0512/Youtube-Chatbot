import pytest

from app.youtube import extract_video_id


def test_extract_watch_url():

    url = (
        "https://www.youtube.com/"
        "watch?v=dQw4w9WgXcQ"
    )

    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_extract_short_url():

    url = "https://youtu.be/dQw4w9WgXcQ"

    assert extract_video_id(url) == "dQw4w9WgXcQ"


def test_invalid_url():

    with pytest.raises(ValueError):

        extract_video_id(
            "https://example.com/video"
        )