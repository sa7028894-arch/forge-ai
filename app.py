import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os

# --- REAL BACKEND IMPORTS ---
from src.vision import detect_part_in_image 
from src.ingest import query_local_documents

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ForgeAI - Industrial Intelligence Dashboard",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. SIDEBAR NAVIGATION & METRICS ---
with st.sidebar:
    st.title("⚙️ ForgeAI Engine Panel")
    st.subheader("System Status")
    st.success("Vision Core: Active (YOLOv8)")
    st.success("Knowledge Core: Active (LangChain)")
    
    # --- DYNAMIC ENVIRONMENT LOGIC ---
    # This checks for the 'APP_ENV' variable on Render. 
    # If not found (like when running locally), it defaults to Windows.
    app_env = os.getenv('APP_ENV', 'Windows Local (Air-Gapped)')
    st.info(f"Environment: {app_env}")
    
    st.divider()
    st.markdown("### Active Dataset Context")
    st.caption("Target Domain: Fadal CNC Components")
    st.caption("Manual Indexing: Fully Loaded")

# --- 3. MAIN DASHBOARD HEADER ---
st.title("ForgeAI: Multimodal Industrial Operations Hub")
st.markdown("Integrating real-time computer vision analysis with semantic engineering documentation retrieval.")
st.divider()

# --- 4. DUAL-PANEL LAYOUT ---
col1, col2 = st.columns([1, 1], gap="large")

# --- LEFT PANEL: COMPUTER VISION ENGINE ---
with col1:
    st.header("📸 Real-Time Vision Inspection")
    st.subheader("Upload Component Snapshot")
    
    uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])
    
    detected_component = ""
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.subheader("Analysis Stream")
        
        # --- EXECUTING REAL YOLO MODEL ---
        with st.spinner("Executing YOLOv8 inference pipeline..."):
            processed_img, detected_component = detect_part_in_image(image)
            
        st.image(processed_img, caption="Processed Image Feed (Bounding Boxes Rendered)", use_container_width=True)
        st.metric(label="Primary Classification Identified", value=detected_component)
    else:
        st.info("Awaiting input image stream to trigger visual spatial bounding pipeline.")

# --- RIGHT PANEL: LANGCHAIN KNOWLEDGE BASE ---
with col2:
    st.header("🧠 Automated Technical RAG Interface")
    st.subheader("Semantic Document Expert Queries")

    # Chat UI Container
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "System initialized. Ask any maintenance, torque, or workflow question regarding indexed Fadal hardware manuals."}]

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # --- VISION-TRIGGERED CONTEXT INJECTION (AUTOMATED QUERY) ---
    if detected_component and detected_component.strip():
        if "last_detected" not in st.session_state or st.session_state.last_detected != detected_component:
            st.session_state.last_detected = detected_component
            
            # The AI "sees" the part and formulates an automated question
            automated_prompt = f"Automated scan detected: {detected_component}. Provide maintenance overview."
            st.session_state.messages.append({"role": "user", "content": automated_prompt})
            
            with st.spinner("Querying vector index for localized hardware schemas..."):
                ai_response = query_local_documents(automated_prompt)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                st.rerun()

    # --- USER INPUT QUERY BOX (MANUAL QUERY) ---
    if prompt := st.chat_input("Ask a manual question (e.g., 'What is the standard tolerance check for the spindle?')..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("Searching document vector embeddings..."):
            response = query_local_documents(prompt)
            
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})