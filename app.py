import streamlit as st
from syllabus_parser import extract_topics
from resource_finder import get_youtube_videos
from schedule_generator import generate_schedule
import fitz  # PyMuPDF

st.title("📚  aaaa Smart Syllabus Navigator")
st.subheader("Your AI-powered study planner")

# --- Input Section ---
input_type = st.radio("Choose input type:", ["Paste Text", "Upload PDF"])
syllabus_text = ""

if input_type == "Paste Text":
    syllabus_text = st.text_area("Paste your syllabus here:", height=200)

elif input_type == "Upload PDF":
    pdf_file = st.file_uploader("Upload syllabus PDF", type=["pdf"])
    if pdf_file:
        # Read PDF text
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        for page in doc:
            syllabus_text += page.get_text()
        st.success("PDF uploaded and read successfully!")

exam_days = st.slider("How many days until your exam?", 7, 60, 30)

if st.button("🚀 Generate My Study Plan") and syllabus_text:
    with st.spinner("AI is analyzing your syllabus..."):

        # Step 1: Extract topics
        topics = extract_topics(syllabus_text)
        st.subheader("📋 Topics Found:")
        for t in topics:
            st.write(f"• {t}")

        # Step 2: Find resources
        st.subheader("🎥 Learning Resources:")
        for topic in topics[:5]:  # limit to 5 topics for speed
            st.markdown(f"**{topic}**")
            videos = get_youtube_videos(topic)
            for v in videos:
                st.markdown(f"- [▶ {v['title']}]({v['url']})")

        # Step 3: Generate schedule
        st.subheader("📅 Your Study Schedule:")
        schedule = generate_schedule(topics, exam_days)
        st.markdown(schedule)
