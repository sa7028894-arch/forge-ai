import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

# --- REAL BACKEND IMPORTS ---
from src.vision import detect_part_in_image 
from src.ingest import query_local_documents

# --- 1. VIBRANT CSS INJECTION ---
def inject_custom_css():
    st.markdown("""
    <style>
    /* Circuit Board Background */
    .stApp {
        background-color: #070910;
        background-image: 
            linear-gradient(90deg, rgba(30, 30, 30, 0.05) 1px, transparent 1px), 
            linear-gradient(0deg, rgba(30, 30, 30, 0.05) 1px, transparent 1px);
        background-size: 40px 40px;
    }

    /* Vibrant Gradient Cards */
    [data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }

    /* Sidebar Background */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }

    /* Vibrant Text Headers */
    h1, h2, h3 {
        background: linear-gradient(90deg, #00f2fe, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }

    /* Colorful Button */
    div.stButton > button {
        background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
    }
    
    /* Environment Box */
    .stInfo {
        background-color: #ff9a9e !important;
        color: #2d3436 !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ForgeAI - Industrial Intelligence",
    page_icon="⚙️",
    layout="wide"
)
inject_custom_css()

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("⚙️ ForgeAI Engine")
    st.markdown("---")
    st.subheader("System Status")
    
    st.write("🟢 Vision Core: Active")
    st.write("🟢 Knowledge Core: Active")
    
    app_env = os.getenv('APP_ENV', 'Windows Local (Air-Gapped)')
    st.info(f"Environment: {app_env}")
    
    st.markdown("---")
    st.markdown("### Active Dataset")
    st.caption("Target Domain: Fadal CNC Components")

# --- 4. MAIN DASHBOARD ---
st.title("ForgeAI: Industrial Operations Hub")
st.markdown("Integrating real-time vision analysis with semantic documentation.")
st.divider()

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.header("📸 Real-Time Vision Inspection")
    uploaded_file = st.file_uploader("Upload Component Snapshot...", type=["jpg", "jpeg", "png"])
    
    detected_component = ""
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with st.spinner("Processing image..."):
            processed_img, detected_component = detect_part_in_image(image)
        st.image(processed_img, use_container_width=True)
        st.metric(label="Detected", value=detected_component)
    else:
        st.info("Awaiting input stream...")

with col2:
    st.header("🧠 Technical RAG Interface")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "System ready. Ask any maintenance question."}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if detected_component and detected_component.strip():
        if "last_detected" not in st.session_state or st.session_state.last_detected != detected_component:
            st.session_state.last_detected = detected_component
            automated_prompt = f"Maintenance overview for: {detected_component}."
            st.session_state.messages.append({"role": "user", "content": automated_prompt})
            
            with st.spinner("Querying vector index..."):
                ai_response = query_local_documents(automated_prompt)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.rerun()

    if prompt := st.chat_input("Ask a manual question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.spinner("Searching..."):
            response = query_local_documents(prompt)
        with st.chat_message("assistant"): st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})