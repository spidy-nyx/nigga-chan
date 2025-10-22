import streamlit as st
import cv2
import numpy as np
from PIL import Image
import random

# Detection modes
FLIRTY_MESSAGES = [
    {
        "title": "✨ Absolute Perfection Detected ✨",
        "message": "Analysis complete: You're stunning beyond measure!",
        "detail": "Beauty level: Off the charts 💕"
    },
    {
        "title": "🌟 Radiance Alert 🌟",
        "message": "Warning: Gorgeousness overload detected!",
        "detail": "Your glow is blinding the camera 😍"
    },
    {
        "title": "💖 Heart-Stealer Identified 💖",
        "message": "Scan complete: Certified heartbreaker status!",
        "detail": "Confidence level: Maximum ✨"
    }
]

FUNNY_MESSAGES = [
    {
        "title": "🚨 FBI ALERT 🚨",
        "message": "WANTED: NIGGA found !",
        "detail": "Reward: you gonna get 3 whip from me 🎯"
    },
    {
        "title": "⚠️ SYSTEM ERROR ⚠️",
        "message": "ERROR 404: NIGGA found !",
        "detail": "Camera malfunction 🤖"
    },
    {
        "title": "🔬 SCIENTIFIC ANALYSIS 🔬",
        "message": "Specimen contains 100% nigga energy!",
        "detail": "nigga gene confirmed 🎬"
    }
]

def detect_face(image):
    """Simple face detection"""
    img_array = np.array(image)
    img_rgb = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    if len(faces) == 0:
        return None, img_array
    
    face = max(faces, key=lambda rect: rect[2] * rect[3])
    x, y, w, h = face
    
    output_img = img_array.copy()
    cv2.rectangle(output_img, (x, y), (x+w, y+h), (255, 0, 255), 3)
    
    return face, output_img

def main():
    st.set_page_config(page_title="Face Analyzer", page_icon="🎯", layout="centered")
    
    # Simple header
    st.title("🎯 Advanced Face Analyzer")
    st.markdown("*Powered by AI Technology*")
    
    # Mode selection
    col1, col2 = st.columns(2)
    with col1:
        mode = st.radio("Select Mode:", ["💕 Flirty", "😂 Funny"], label_visibility="collapsed")
    
    # File uploader
    st.markdown("---")
    uploaded_file = st.file_uploader("Upload a photo", type=['jpg', 'jpeg', 'png'])
    
    # Camera option
    use_camera = st.checkbox("📷 Use Camera")
    if use_camera:
        camera_img = st.camera_input("Take a photo")
        if camera_img:
            uploaded_file = camera_img
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        
        # Show original
        st.image(image, caption="Analyzing...", use_container_width=True)
        
        # Detect face
        with st.spinner("🔍 Running analysis..."):
            face, output_img = detect_face(image)
        
        if face is not None:
            # Show result with box
            st.image(output_img, use_container_width=True)
            
            # Select random message based on mode
            if "Flirty" in mode:
                result = random.choice(FLIRTY_MESSAGES)
                color = "#FF69B4"
            else:
                result = random.choice(FUNNY_MESSAGES)
                color = "#FFD700"
            
            # Display result
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                        padding: 30px; border-radius: 15px; border: 3px solid {color}; 
                        text-align: center; margin: 20px 0;'>
                <h2 style='color: {color}; margin: 0;'>{result['title']}</h2>
                <h3 style='margin: 15px 0;'>{result['message']}</h3>
                <p style='font-size: 18px; margin: 10px 0;'>{result['detail']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Fun stats
            st.markdown("### 📊 Analysis Report")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Awesomeness", "100%", "📈")
            with col2:
                st.metric("Confidence", "∞", "🚀")
            with col3:
                st.metric("Vibes", "Immaculate", "✨")
            
        else:
            st.error("❌ No face detected! Please try another photo with a clear face.")
    
    else:
        st.info("👆 Upload a photo or use camera to start")
    
    # Footer
    st.markdown("---")
    st.markdown("<center><small>Just for fun! 😄</small></center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
