import logging
from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

try:
    from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptAvailable
    logging.debug("Successfully imported youtube_transcript_api")
except ImportError as e:
    logging.error(f"Error importing youtube_transcript_api: {str(e)}")
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
        logging.error("YouTube Transcript API is not available")
        return jsonify({'error': 'YouTube Transcript API is not available'}), 500

    url = request.json['url']
    video_id = get_video_id(url)
    
    if not video_id:
        logging.warning(f"Invalid YouTube URL: {url}")
        return jsonify({'error': 'Invalid YouTube URL'}), 400
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatted_transcript = ' '.join([entry['text'] for entry in transcript])
        logging.info(f"Successfully retrieved transcript for video ID: {video_id}")
        return jsonify({'transcript': formatted_transcript})
    except (TranscriptsDisabled, NoTranscriptAvailable) as e:
        logging.warning(f"No transcript available for video ID {video_id}: {str(e)}")
        return jsonify({'error': 'No transcript available for this video'}), 404
    except Exception as e:
        logging.error(f"Error retrieving transcript for video ID {video_id}: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
