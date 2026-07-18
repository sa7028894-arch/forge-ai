import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

# --- REAL BACKEND IMPORTS ---
from src.vision import detect_part_in_image 
from src.ingest import query_local_documents

# --- 1. CSS INJECTION FOR AESTHETICS ---
def inject_custom_css():
    st.markdown("""
    <style>
    /* Dark Theme Base */
    .stApp {
        background-color: #0e1117;
    }
    
    /* Modern Container Cards */
    [data-testid="stVerticalBlock"] {
        background-color: #1a1c22;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0e1117;
        border-right: 1px solid #333;
    }
    
    /* Professional Headers */
    h1, h2, h3 {
        color: #e0e0e0 !important;
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Chat Input styling */
    .stChatInput {
        background-color: #262730;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ForgeAI - Industrial Intelligence Dashboard",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)
inject_custom_css()

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("⚙️ ForgeAI Engine")
    st.markdown("---")
    st.subheader("System Status")
    
    # Clean Status Indicators
    col_v1, col_v2 = st.columns([1, 5])
    with col_v1: st.write("🟢")
    with col_v2: st.write("Vision Core: Active")
    
    col_k1, col_k2 = st.columns([1, 5])
    with col_k1: st.write("🟢")
    with col_k2: st.write("Knowledge Core: Active")
    
    # Dynamic Environment
    app_env = os.getenv('APP_ENV', 'Windows Local (Air-Gapped)')
    st.info(f"Environment: {app_env}")
    
    st.markdown("---")
    st.markdown("### Active Dataset")
    st.caption("Target Domain: Fadal CNC Components")
    st.caption("Status: Fully Loaded")

# --- 4. MAIN DASHBOARD ---
st.title("ForgeAI: Industrial Operations Hub")
st.markdown("Integrating real-time computer vision analysis with semantic engineering documentation.")
st.divider()

col1, col2 = st.columns([1, 1], gap="large")

# --- LEFT PANEL: VISION ENGINE ---
with col1:
    st.header("📸 Real-Time Vision Inspection")
    uploaded_file = st.file_uploader("Upload Component Snapshot...", type=["jpg", "jpeg", "png"])
    
    detected_component = ""
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with st.spinner("Processing image..."):
            processed_img, detected_component = detect_part_in_image(image)
            
        st.image(processed_img, caption="Bounding Boxes Rendered", use_container_width=True)
        st.metric(label="Primary Classification", value=detected_component)
    else:
        st.info("Awaiting input stream...")

# --- RIGHT PANEL: RAG KNOWLEDGE BASE ---
with col2:
    st.header("🧠 Technical RAG Interface")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "System initialized. Ask any maintenance question regarding Fadal manuals."}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Vision Trigger
    if detected_component and detected_component.strip():
        if "last_detected" not in st.session_state or st.session_state.last_detected != detected_component:
            st.session_state.last_detected = detected_component
            automated_prompt = f"Automated scan detected: {detected_component}. Provide maintenance overview."
            st.session_state.messages.append({"role": "user", "content": automated_prompt})
            
            with st.spinner("Querying vector index..."):
                ai_response = query_local_documents(automated_prompt)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.rerun()

    # Manual Input
    if prompt := st.chat_input("Ask a manual question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.spinner("Searching document embeddings..."):
            response = query_local_documents(prompt)
            
        with st.chat_message("assistant"): st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})