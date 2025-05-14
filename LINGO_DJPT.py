import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os
import tempfile

# Set page configuration
st.set_page_config(page_title="LINGO_DJPT", layout="centered", initial_sidebar_state="collapsed")

# Custom responsive header
st.markdown("""
    <style>
        .header-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 10px 20px;
            margin-top: 20px;
            margin-bottom: 30px;
            background-color: #f8f9fa;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        }
        .main-header {
            font-size: 2.5em;
            font-weight: 800;
            color: #2c3e50;
            margin: 0 10px;
        }
        .sub-header {
            font-size: 1.2em;
            font-weight: 500;
            color: #666;
            margin: 0 10px;
        }
        @media screen and (max-width: 768px) {
            .main-header {
                font-size: 1.8em;
            }
            .sub-header {
                font-size: 1em;
                margin-top: 4px;
            }
        }
        @media screen and (max-width: 480px) {
            .header-container {
                flex-direction: column;
                gap: 6px;
            }
            .main-header {
                font-size: 1.6em;
            }
            .sub-header {
                font-size: 0.95em;
            }
        }
    </style>
    <div class="header-container">
        <div class="main-header">🗣 LINGO_DJPT</div>
        <div class="sub-header">SVUD_P2</div>
    </div>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("## 🌍 Translate and Speak")
st.markdown("Easily translate any text and listen to it using Text-to-Speech.")

# Text input
text_input = st.text_area("Enter text to translate:", height=150)

# Language dictionary
langs = {
    "English": "en","Hindi": "hi", "French": "fr", "Spanish": "es", "German": "de",
    "Tamil": "ta", "Bengali": "bn", "Japanese": "ja", "Russian": "ru",
    "Arabic": "ar", "Chinese": "zh-cn", "Korean": "ko", "Italian": "it"
}

# Language selection
col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source Language", list(langs.keys()), index=0)
with col2:
    tgt_lang = st.selectbox("Target Language", list(langs.keys()), index=1)

# Translation and audio
if st.button("🔁 Translate & Speak"):
    if text_input:
        with st.spinner("Translating and generating audio..."):
            translator = Translator()
            translated = translator.translate(text_input, src=langs[src_lang], dest=langs[tgt_lang])
            st.success(f"Translated Text ({tgt_lang}):")
            st.markdown(f"### \"{translated.text}\"")

            tts = gTTS(text=translated.text, lang=langs[tgt_lang])
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
                tts.save(tf.name)
                st.audio(tf.name, format='audio/mp3')

                # Read file as binary and allow download
                with open(tf.name, "rb") as audio_file:
                    audio_bytes = audio_file.read()

                st.download_button(
                    label="🔽 Download MP3",
                    data=audio_bytes,
                    file_name="LINGO_DJPT_translation.mp3",
                    mime="audio/mpeg"
                )
    else:
        st.warning("Please enter text to translate.")

# Footer
st.markdown("""
    <hr style='margin-top:40px;'>
    <div style='text-align: center; color: gray;'>
        🌍 LINGO_DJPT • SVUD_P2 • Powered by Python, Streamlit, Google Translate API, and gTTS
    </div>
""", unsafe_allow_html=True)
