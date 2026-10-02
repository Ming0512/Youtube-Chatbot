import re
from youtube_transcript_api import YouTubeTranscriptApi 

def extract_video_id(url: str) -> str:
    """Extract the 11-characters Youtube video ID from url"""
    patterns =[
        r"(?:youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})",
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"(?:youtube\.com/shorts/)([a-zA-Z0-9_-]{11})",
        r"(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("Invalid YouTube URL")

def get_transcript(video_id:str) -> str:
    """Fetch the English transcript and return it as plain text."""
    
    api = YouTubeTranscriptApi()
    transcripts = api.fetch(
        video_id, languages=['en']
    )
    
    text = " ".join(snippet.text for snippet in transcripts)
    return text