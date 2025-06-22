# filepath: c:\Users\Admin\Documents\PROJECTS\youtube-summarizer\src\app.py
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="YouTube Summarizer Bot", page_icon=":robot_face:", layout="centered")
st.markdown(
    """
    <style>
    .main {background-color: #f8fafc;}
    .stButton>button {background-color: #2563eb; color: white; font-weight: bold; border-radius: 8px;}
    .stTextInput>div>div>input {border-radius: 8px;}
    .stMarkdown h1 {color: #2563eb;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🤖 YouTube Summarizer Bot")
st.write("Paste a YouTube video URL below and get a concise summary powered by Gemini Pro 2.0.")

youtube_url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
summarize_btn = st.button("Summarize Video")

if summarize_btn:
    if not GEMINI_API_KEY or GEMINI_API_KEY == "YOUR_GEMINI_API_KEY":
        st.error("Please set your Gemini API key in src/env.py.")
    elif not youtube_url:
        st.error("Please enter a YouTube video URL.")
    else:
        try:
            # Extract video ID
            if "v=" in youtube_url:
                video_id = youtube_url.split("v=")[1].split("&")[0]
            elif "youtu.be/" in youtube_url:
                video_id = youtube_url.split("youtu.be/")[1].split("?")[0]
            else:
                st.error("Invalid YouTube URL format.")
                st.stop()

            # Get transcript
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = " ".join([x['text'] for x in transcript])

            # LangChain + Gemini 2.0 Flash
            llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY)
            prompt = PromptTemplate(
                input_variables=["transcript"],
                template="Summarize the following YouTube video transcript in a concise, clear paragraph:\n{transcript}"
            )
            message = prompt.format(transcript=transcript_text)
            with st.spinner("Summarizing..."):
                try:
                    response = llm.invoke([{"role": "user", "content": message}])
                    # If response is a Message object, get the content
                    summary_text = getattr(response, "content", str(response))
                    # Remove unwanted prefix/suffix if present
                    if summary_text.startswith("content="):
                       summary_text = summary_text[len("content="):].strip().strip('"')
                    summary_text = summary_text.replace("\\n", "\n").strip()

                    st.success("Summary:")
                    st.markdown(
                        f"<div style='background:#e0e7ff;padding:16px;border-radius:8px;color:#222;white-space:pre-line;'>{summary_text}</div>",
                        unsafe_allow_html=True
                    )
                except Exception as e:
                    st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Failed to retrieve transcript: {e}")