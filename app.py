import streamlit as st
from transformers import pipeline

st.title("📝 AI Text Summarizer")

st.write("Enter text below to generate summary")

# Load model
@st.cache_resource
def load_model():
    return pipeline(task="summarization", model="sshleifer/distilbart-cnn-12-6")

summarizer = load_model()

# Input text
text = st.text_area("Enter text:")

# Button
if st.button("Summarize"):
    if text:
        summary = summarizer(
            text,
            max_length=130,
            min_length=30,
            do_sample=False
        )
        
        st.subheader("📌 Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text")
