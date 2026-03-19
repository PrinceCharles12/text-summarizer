import streamlit as st

st.title("📝 AI Text Summarizer")

st.write("Enter text below to generate summary")

# Input text
text = st.text_area("Enter text:")

# Simple summarization function
def summarize_text(text):
    sentences = text.split(".")
    summary = ".".join(sentences[:2])  # take first 2 sentences
    return summary

# Button
if st.button("Summarize"):
    if text:
        summary = summarize_text(text)
        
        st.subheader("📌 Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text")
