from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_transcript(video_id):
    """Fetch transcript from YouTube video and print the full text."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = " ".join([entry['text'] for entry in transcript])
        print("\n=== 📜 Full Transcript ===\n")
        print(full_transcript)
    except Exception as e:
        print(f"❌ Error fetching transcript: {e}")

def extract_video_id(url):
    """Extract YouTube video ID from multiple URL formats."""
    match = re.search(r"(?:v=|youtu\.be/|embed/|shorts/|watch\?v=)([\w-]+)", url)
    if match:
        return match.group(1)
    return None

def main():
    video_id = 'ivy1sII_UnA'
    
    print(f"✅ Video ID: {video_id}")
    print("📜 Fetching transcript...")
    get_transcript(video_id)

if __name__ == "__main__":
    main()