import streamlit as st

st.set_page_config(
    page_title="About | AlphaNet",
    page_icon="ℹ️",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00FF9F;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# ABOUT PAGE
# =========================================================
st.title("ℹ️ About AlphaNet")

st.markdown("""
## 🛡️ AlphaNet

AlphaNet is a Streamlit-based Network Utility & Monitoring Suite designed for real-time diagnostics and monitoring.

---

## 🚀 Features

### 🌐 Website Monitoring
Checks:
- Website availability
- Response time
- Status code

### 📥 Bulk Downloader
Downloads:
- Images
- PDFs
- Files
- Assets from direct URLs

### ⚡ Speed Test
Measures:
- Download speed
- Upload speed
- Ping latency

---

## 👨‍💻 Team

### 🚀 Team Name:
ALPHA PAIR

### 🏷️ Tagline:
**Monitor. Analyze. Optimize.**
""")
