import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="AI Business Strategist", page_icon="📈", layout="centered")

# Custom CSS to hide the GitHub icon and style the app
custom_css = """
<style>
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    h1 { color: #1E3A8A; text-align: center; }
    .subtitle { text-align: center; font-size: 1.1rem; color: #4B5563; margin-bottom: 2rem; }
    div.stButton > button:first-child { 
        background-color: #2563EB; color: white; border-radius: 8px; width: 100%; 
        padding: 12px; font-size: 18px; font-weight: bold; border: none; 
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# API Configuration
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("API Key not found.")
    st.stop()

# Interface
st.title("📈 AI Business Strategist")
st.markdown('<p class="subtitle">Instant branding, slogans, and growth strategies for your hustle.</p>', unsafe_allow_html=True)

business_desc = st.text_area("Describe your business:", height=120)

if st.button("Generate Strategy 🚀"):
    if business_desc:
        with st.spinner("Analyzing your business model..."):
            model = genai.GenerativeModel('gemini-3.8-flash')
            prompt = f"Act as an expert business consultant. Business: {business_desc}. Provide: 1. Three catchy names. 2. A marketing slogan. 3. Three low-cost growth strategies."
            response = model.generate_content(prompt)
            st.success("Strategy Generated Successfully!")
            st.markdown(response.text)
    else:
        st.warning("Please describe your business first.")
