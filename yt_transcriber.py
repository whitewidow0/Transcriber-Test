from flask import Flask, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import re
import os

def create_app():
    application = Flask(__name__)

    def get_transcript(video_id):
        """Fetch transcript from YouTube video."""
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_transcript = " ".join([entry['text'] for entry in transcript])
            return full_transcript
        except Exception as e:
            return f"Error fetching transcript: {e}"

    def extract_video_id(url):
        """Extract YouTube video ID from multiple URL formats."""
        match = re.search(r"(?:v=|youtu\.be/|embed/|shorts/|watch\?v=)([\w-]+)", url)
        if match:
            return match.group(1)
        return None

    @application.route('/')
    def index():
        video_id = 'ivy1sII_UnA'
        transcript = get_transcript(video_id)
        return jsonify({
            "video_id": video_id,
            "transcript": transcript
        })

    return application

if __name__ == '__main__':
    application = create_app()
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)