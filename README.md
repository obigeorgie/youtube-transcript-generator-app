# YouTube Transcript Generator

A Flask-based web application that fetches and displays transcripts from YouTube videos using a clean, responsive interface.

## Features

- Extract transcripts from YouTube videos using video URLs
- Support for various YouTube URL formats
- Clean and responsive UI using Tailwind CSS
- Copy transcript to clipboard functionality
- Error handling for invalid URLs and unavailable transcripts

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, JavaScript, Tailwind CSS
- API: youtube-transcript-api

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:
```bash
python main.py
```

## Usage

1. Visit the application in your web browser
2. Paste a YouTube video URL into the input field
3. Click "Get Transcript" to fetch the video transcript
4. Use the "Copy to Clipboard" button to copy the transcript

## Custom Domain Setup

Detailed instructions for setting up a custom domain can be found in [custom_domain_setup.md](custom_domain_setup.md).

## License

MIT License
