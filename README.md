# YouTube Summarizer

This project is a YouTube Summarizer application that allows users to input a YouTube video URL and receive a concise summary of the video's content. The application is built using Streamlit and utilizes the YouTube Transcript API along with the Gemini Pro 2.0 model for summarization.

## Features

- Input a YouTube video URL to retrieve its transcript.
- Summarize the transcript into a clear and concise paragraph.
- User-friendly interface powered by Streamlit.

## Requirements

To run this project, you need to have Python installed on your machine. It is recommended to use a virtual environment to manage dependencies.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd youtube-summarizer
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```
   streamlit run src/app.py
   ```

## Usage

- Open the application in your web browser.
- Paste a YouTube video URL into the input field.
- Click the "Summarize Video" button to receive a summary of the video.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.