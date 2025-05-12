import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile

# Page config
st.set_page_config(
    page_title="LINGO_DJPT",
    page_icon="🗣️",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
    <style>
        .stApp {
            background-color: #grey;
        }
        .header-container {
            display: flex;
            justify-content: center;
            align-items: baseline;
            gap: 10px;
            margin-top: 30px;
            margin-bottom: 20px;
        }
        .main-header {
            font-size: 3em;
            font-weight: 800;
            text-align: center;
            color: #2c3e50;
            margin-top: 20px;
        }
        .sub-header {
            font-size: 1.2em;
            font-weight: 500;
            text-align: center;
            color: #888;
            margin-bottom: 30px;
        }
        .translated-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.05);
            font-size: 1.3em;
            font-weight: 500;
            color: #2c3e50;
        }
        .copy-button {
            background-color: #2ecc71;
            color: white;
            font-size: 1em;
            padding: 8px 20px;
            border: none;
            border-radius: 5px;
            margin-top: 15px;
            cursor: pointer;
        }
        .copy-button:hover {
            background-color: #27ae60;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #999;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<div class='header-container'><div class='main-header'>🗣️ LINGO_DJPT</div><div class='sub-header'>-SVUD_P2</div></div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Translate & Speak in Any Language</div>", unsafe_allow_html=True)

# Language options
languages = {
    "Hindi": "hi", "French": "fr", "Spanish": "es", "German": "de",
    "Tamil": "ta", "Bengali": "bn", "Japanese": "ja", "Russian": "ru",
    "Arabic": "ar", "Chinese": "zh-cn", "Korean": "ko", "Italian": "it"
}

# Input section
st.markdown("### ✍️ Enter English Text:")
text_input = st.text_area("", height=180, placeholder="Type your sentence here...")

target_lang = st.selectbox("🌐 Choose Translation Language:", options=list(languages.keys()), index=0)

translator = Translator()

if st.button("🚀 Translate & Speak", help="Click to translate and generate audio"):
    if not text_input.strip():
        st.warning("⚠️ Please enter text before translating.")
    else:
        with st.spinner("🔄 Translating and generating speech..."):
            lang_code = languages[target_lang]
            translated_text = translator.translate(text_input, dest=lang_code).text

            # Output
            st.markdown("### ✅ Translation:")
            st.markdown(f"<div class='translated-box'>{translated_text}</div>", unsafe_allow_html=True)

            # Copy to clipboard
            st.markdown(f"""
                <button class="copy-button" onclick="navigator.clipboard.writeText(`{translated_text}`)">
                    📋 Copy Translation
                </button>
            """, unsafe_allow_html=True)

            # TTS Audio Output
            try:
                tts = gTTS(text=translated_text, lang=lang_code)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                    tts.save(tmpfile.name)
                    st.audio(tmpfile.name, format="audio/mp3")
            except Exception as e:
                st.error(f"🔊 Error generating audio: {e}")

# Footer
st.markdown("<div class='footer'>🌍 LINGO_DJPT • SVUD_P2 • Powered by Python, Streamlit, Google Translate API, and gTTS</div>", unsafe_allow_html=True)
