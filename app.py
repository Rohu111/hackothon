import streamlit as st

st.set_page_config(
    page_title="AlphaNet",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# GLOBAL CSS
# =========================================================
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0E1117;
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #161B22;
}

/* Metric Cards */
div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #00C8FF;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 0px 12px rgba(0,200,255,0.4);
}

/* Headers */
h1, h2, h3 {
    color: #00FF9F;
}

/* Buttons */
.stButton > button {
    background-color: #00C8FF;
    color: black;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
    border: none;
    padding: 10px;
}

/* Inputs */
.stTextInput > div > div > input {
    background-color: #1E1E1E;
    color: white;
}

textarea {
    background-color: #1E1E1E !important;
    color: white !important;
}

label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LANDING PAGE
# =========================================================
st.title("🛡️ AlphaNet")
st.subheader("Network Utility & Monitoring Suite")

st.markdown("""
## 🚀 Welcome to AlphaNet

A cybersecurity-inspired real-time network toolkit built using Streamlit.

### Features
- 🌐 Website Monitoring
- 📥 Bulk File Downloader
- ⚡ Real-Time Internet Speed Test
- 📊 Network Diagnostics Dashboard

---

Use the sidebar to navigate through the modules.
""")

st.success("🟢 AlphaNet System Online")
