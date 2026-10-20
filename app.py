import streamlit as st
import google.generativeai as genai

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("API Key not found. Please add GEMINI_API_KEY to your secrets.")
    st.stop()

st.set_page_config(page_title="AI Business Strategist", page_icon="📈")
st.title("📈 AI Business Strategist")
st.write("Enter your business operation details below to get instant branding and growth strategies powered by Gemini.")

business_desc = st.text_area(
    "Describe your business:",
    placeholder="e.g., I operate a fleet of commercial motorcycles and want to increase daily revenue..."
)

if st.button("Generate Strategy"):
    if business_desc:
        with st.spinner("Analyzing your business model..."):
            try:
                model = genai.GenerativeModel('gemini-3.8-flash')
                prompt = f"""
                Act as an expert business consultant. I have the following business operation: {business_desc}. 
                Please provide:
                1. Three catchy, professional business names.
                2. A short, impactful marketing slogan.
                3. Three highly specific, low-cost strategies to maximize daily revenue and customer retention.
                """
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please describe your business first.")
