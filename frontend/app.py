import streamlit as st
import requests
import json

# Streamlit frontend for MVP
st.set_page_config(page_title="NeuroHub AI Assistant", layout="wide")

st.title("🧠 NeuroHub AI Assistant")
st.markdown("*Supporting neurodivergent users with AI-powered tools*")

# Sidebar navigation
feature = st.sidebar.selectbox(
    "Choose Feature",
    ["Voice Journaling", "Focus Planner", "Emotional Coach", "AR Reader"]
)

API_BASE = "http://localhost:8000"

if feature == "Voice Journaling":
    st.header("🎤 Voice Journaling → Mind Maps")
    
    uploaded_audio = st.file_uploader("Upload audio file", type=['wav', 'mp3', 'm4a'])
    
    if uploaded_audio and st.button("Process Audio"):
        with st.spinner("Processing..."):
            files = {"audio": uploaded_audio}
            response = requests.post(f"{API_BASE}/voice/transcribe", files=files)
            
            if response.status_code == 200:
                data = response.json()
                st.subheader("Transcription")
                st.write(data["transcription"])
                
                st.subheader("Mind Map")
                st.components.v1.html(data["mindmap"], height=500)

elif feature == "Focus Planner":
    st.header("📅 Focus-Friendly Planner")
    
    task_input = st.text_input("Add task (natural language)", 
                              placeholder="remind me to do math at 3pm")
    
    if st.button("Add Task"):
        response = requests.post(f"{API_BASE}/planner/add-task", 
                               json={"text": task_input})
        if response.status_code == 200:
            st.success("Task added!")
    
    if st.button("Show Tasks"):
        response = requests.get(f"{API_BASE}/planner/tasks")
        if response.status_code == 200:
            tasks = response.json()["tasks"]
            for task in tasks:
                st.write(f"- {task['title']} (Due: {task['due_date']})")

elif feature == "Emotional Coach":
    st.header("❤️ Emotional Coach")
    
    feeling_text = st.text_area("How are you feeling?", 
                               placeholder="I'm feeling anxious about tomorrow...")
    
    if st.button("Analyze Emotion"):
        response = requests.post(f"{API_BASE}/coach/analyze-emotion", 
                               json={"text": feeling_text})
        if response.status_code == 200:
            data = response.json()
            st.write(f"**Detected Emotion:** {data['emotion']['emotion']}")
            st.write(f"**Suggestion:** {data['suggestion']}")

elif feature == "AR Reader":
    st.header("📷 AR Reading Assist")
    
    uploaded_image = st.file_uploader("Upload image with text", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_image and st.button("Read Image"):
        files = {"image": uploaded_image}
        response = requests.post(f"{API_BASE}/ar/read-image", files=files)
        
        if response.status_code == 200:
            data = response.json()
            st.subheader("Original Text")
            st.write(data["original_text"])
            
            st.subheader("Simplified Text")
            st.write(data["simplified_text"])
            
            if st.button("Read Aloud"):
                tts_response = requests.post(f"{API_BASE}/ar/text-to-speech", 
                                           params={"text": data["simplified_text"]})
                if tts_response.status_code == 200:
                    st.audio(tts_response.content)