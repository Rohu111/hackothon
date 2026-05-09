import streamlit as st

st.set_page_config(
    page_title="Home | AlphaNet",
    page_icon="🏠",
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

[data-testid="stSidebar"] {
    background-color: #161B22;
}

div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #00C8FF;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 0px 12px rgba(0,200,255,0.4);
}

h1, h2, h3 {
    color: #00FF9F;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HOME PAGE
# =========================================================
st.title("🏠 AlphaNet Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌐 Active Services", "3")

with col2:
    st.metric("⚡ Network Status", "ONLINE")

with col3:
    st.metric("📡 Average Ping", "12 ms")

st.divider()

st.info("Welcome to the AlphaNet real-time network dashboard.")

st.markdown("""
### 🛠️ Available Modules

- 🌐 Website Monitor
- 📥 Bulk Downloader
- ⚡ Real-Time Speed Test

---

### 🎯 Mission

AlphaNet centralizes monitoring, diagnostics, and downloading into one lightweight cybersecurity dashboard.
""")
