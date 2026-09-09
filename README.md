# 🔍 AI Code Review Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-code-review-agent-ga65psh7sybppqfpnpdebr.streamlit.app)

An automated static code analysis agent built with **LangChain** and **Google Gemini** that reviews source code for runtime bugs, security vulnerabilities (e.g., SQL injection), performance bottlenecks, and PEP 8 style violations.

🚀 **Live Demo:** [Try the Web App Here](https://ai-code-review-agent-ga65psh7sybppqfpnpdebr.streamlit.app)

---

## 🛠️ Tech Stack & Frameworks

* **Language:** Python 3.11+
* **Framework:** LangChain (`langchain-google-genai`)
* **LLM Engine:** Google Gemini (`gemini-3.6-flash`)
* **User Interface:** Streamlit & CLI (`argparse`)
* **Environment Management:** `python-dotenv`

---

## 🚀 Quick Start (Local Setup)

### 1. Clone & Install Dependencies
```bash
git clone [https://github.com/Archee01pal/02-code-review-agent.git](https://github.com/Archee01pal/02-code-review-agent.git)
cd 02-code-review-agent
python -m venv venv
# Activate virtual environment
# Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
