import streamlit as st
from transformers import pipeline

st.title("📝 AI Text Summarizer")

st.write("Enter text below to generate summary")

# Load model safely
@st.cache_resource
def load_model():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Initialize summarizer
try:
    summarizer = load_model()
except Exception as e:
    st.error("Model loading failed. Please check logs.")
    st.stop()

# Input text
text = st.text_area("Enter text:")

# Button
if st.button("Summarize"):
    if text:
        try:
            summary = summarizer(
                text,
                max_length=100,
                min_length=20,
                do_sample=False
            )
            
            st.subheader("📌 Summary:")
            st.write(summary[0]['summary_text'])
        except Exception as e:
            st.error("Error during summarization. Try smaller text.")
    else:
        st.warning("Please enter some text")
