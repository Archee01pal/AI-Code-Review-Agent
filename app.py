import os
import streamlit as st
from dotenv import load_dotenv
from agent import review_code

load_dotenv()

st.set_page_config(page_title="AI Code Reviewer", page_icon="🔍", layout="wide")

st.title("🔍 AI Code Review Agent")
st.caption("Powered by LangChain & Google Gemini")

language = st.selectbox("Language", ["python", "javascript", "typescript", "java", "cpp"])

# Choice between pasting code or uploading a file
input_mode = st.radio("Input Method", ["Paste Code", "Upload File"], horizontal=True)

code_input = ""

if input_mode == "Paste Code":
    code_input = st.text_area("Paste your code here:", height=250)
else:
    uploaded_file = st.file_uploader("Choose a code file", type=["py", "js", "ts", "java", "cpp"])
    if uploaded_file is not None:
        code_input = uploaded_file.read().decode("utf-8")
        st.code(code_input, language=language)

if st.button("🚀 Review Code", type="primary"):
    if not code_input.strip():
        st.warning("Please provide code to review.")
    else:
        with st.spinner("Analyzing code for bugs, security risks, and style..."):
            review = review_code(code_input, language=language)
            st.markdown("### 📋 Review Results")
            st.markdown(review)