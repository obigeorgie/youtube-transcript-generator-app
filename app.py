from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api.exceptions import TranscriptsDisabled, NoTranscriptAvailable
except ImportError:
    print("Error: youtube_transcript_api module not found. Please make sure it's installed correctly.")
    YouTubeTranscriptApi = None
    TranscriptsDisabled = Exception
    NoTranscriptAvailable = Exception

def get_video_id(url):
    """Extract the video ID from a YouTube URL."""
    parsed_url = urlparse(url)
    if parsed_url.hostname in ('youtu.be', 'www.youtu.be'):
        return parsed_url.path[1:]
    if parsed_url.hostname in ('youtube.com', 'www.youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
        if parsed_url.path[:7] == '/embed/':
            return parsed_url.path.split('/')[2]
        if parsed_url.path[:3] == '/v/':
            return parsed_url.path.split('/')[2]
    # If the URL format is not recognized
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_transcript', methods=['POST'])
def get_transcript():
    if YouTubeTranscriptApi is None:
        return jsonify({'error': 'YouTube Transcript API is not available'}), 500

    url = request.json['url']
    video_id = get_video_id(url)
    
    if not video_id:
        return jsonify({'error': 'Invalid YouTube URL'}), 400
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatted_transcript = ' '.join([entry['text'] for entry in transcript])
        return jsonify({'transcript': formatted_transcript})
    except (TranscriptsDisabled, NoTranscriptAvailable):
        return jsonify({'error': 'No transcript available for this video'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
