import streamlit as st
import cv2
import numpy as np
from PIL import Image
import random
import time

# Funny messages
FUNNY_MESSAGES = [
    {
        "title": "🚨 ALERT 🚨",
        "message": "WANTED: Amazing GAY NIGGA found!",
        "detail": "Reward: you wanna get 3 whip shot from me  🎯"
    },
    {
        "title": "⚠️ SYSTEM NOTIFICATION ⚠️",
        "message": "NOTIFICATION: Legend LESBIAN detected!",
        "detail": "SYBAU LESBO NIGGA 🤖"
    },
    {
        "title": "🔬 SCIENTIFIC ANALYSIS 🔬",
        "message": "KFC BUCKET CHICKEN KING ",
        "detail": "HE/SHE STOLE 3 LEG PIECE✅"
    }
]

# Flirty messages
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
    cv2.rectangle(output_img, (x, y), (x + w, y + h), (255, 0, 255), 3)

    return face, output_img


def show_funny_popup(message):
    """Display funny message with popup and animation"""
    color = "#FFD700"

    # Popup animation with CSS
    st.markdown(f"""
    <style>
        @keyframes popupBounce {{
            0% {{ transform: scale(0) rotate(-10deg); opacity: 0; }}
            50% {{ transform: scale(1.1); }}
            100% {{ transform: scale(1) rotate(0deg); opacity: 1; }}
        }}

        @keyframes shake {{
            0%, 100% {{ transform: translateX(0); }}
            25% {{ transform: translateX(-5px); }}
            75% {{ transform: translateX(5px); }}
        }}

        .funny-popup {{
            animation: popupBounce 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
            background: linear-gradient(135deg, {color}22 0%, {color}44 100%);
            padding: 40px;
            border-radius: 20px;
            border: 4px solid {color};
            text-align: center;
            margin: 20px 0;
            box-shadow: 0 10px 40px rgba(255, 215, 0, 0.4);
        }}

        .funny-popup h2 {{
            color: {color};
            margin: 0;
            font-size: 2em;
            animation: shake 0.5s;
        }}

        .funny-popup h3 {{
            margin: 15px 0;
            font-size: 1.5em;
        }}

        .funny-popup p {{
            font-size: 18px;
            margin: 10px 0;
        }}
    </style>
    <div class='funny-popup'>
        <h2>{message['title']}</h2>
        <h3>{message['message']}</h3>
        <p>{message['detail']}</p>
    </div>
    """, unsafe_allow_html=True)


def show_flirty_hearts(message):
    """Display flirty message with hearts animation"""
    color = "#FF69B4"

    st.markdown(f"""
    <style>
        @keyframes heartFloat {{
            0% {{ transform: translateY(0) scale(1); opacity: 1; }}
            100% {{ transform: translateY(-150px) scale(0); opacity: 0; }}
        }}

        @keyframes glow {{
            0%, 100% {{ filter: drop-shadow(0 0 5px {color}); }}
            50% {{ filter: drop-shadow(0 0 20px {color}); }}
        }}

        .heart {{
            position: fixed;
            font-size: 2em;
            animation: heartFloat 2s ease-in forwards;
            pointer-events: none;
        }}

        .flirty-popup {{
            background: linear-gradient(135deg, {color}22 0%, {color}44 100%);
            padding: 40px;
            border-radius: 20px;
            border: 4px solid {color};
            text-align: center;
            margin: 20px 0;
            box-shadow: 0 10px 40px rgba(255, 105, 180, 0.4);
            animation: glow 1.5s ease-in-out infinite;
        }}

        .flirty-popup h2 {{
            color: {color};
            margin: 0;
            font-size: 2em;
        }}

        .flirty-popup h3 {{
            margin: 15px 0;
            font-size: 1.5em;
        }}

        .flirty-popup p {{
            font-size: 18px;
            margin: 10px 0;
        }}
    </style>
    <div class='flirty-popup'>
        <h2>{message['title']}</h2>
        <h3>{message['message']}</h3>
        <p>{message['detail']}</p>
    </div>
    """, unsafe_allow_html=True)

    # JavaScript to create floating hearts
    st.markdown("""
    <script>
        function createHearts() {{
            for(let i = 0; i < 8; i++) {{
                const heart = document.createElement('div');
                heart.innerHTML = '💕';
                heart.className = 'heart';
                heart.style.left = Math.random() * 100 + '%';
                heart.style.animation = `heartFloat ${1.5 + Math.random() * 0.5}s ease-in forwards`;
                document.body.appendChild(heart);

                setTimeout(() => heart.remove(), 2500);
            }}
        }}
        createHearts();
    </script>
    """, unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Face Analyzer", page_icon="🎯", layout="centered")

    # Initialize session state for alternating messages
    if 'message_count' not in st.session_state:
        st.session_state.message_count = 0

    # Simple header
    st.title("🎯 Advanced Face Analyzer")
    st.markdown("*Powered by AI Technology*")

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

            # Alternate between funny and flirty messages
            if st.session_state.message_count % 2 == 0:
                # Funny message
                result = random.choice(FUNNY_MESSAGES)
                show_funny_popup(result)
            else:
                # Flirty message
                result = random.choice(FLIRTY_MESSAGES)
                show_flirty_hearts(result)

            st.session_state.message_count += 1

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
