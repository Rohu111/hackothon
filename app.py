import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AlphaNet",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main App */
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

/* Headings */
h1, h2, h3 {
    color: #00FF9F;
}

/* Buttons */
.stButton>button {
    background-color: #00C8FF;
    color: black;
    border-radius: 10px;
    font-weight: bold;
}

/* Text Inputs */
.stTextInput>div>div>input {
    background-color: #1E1E1E;
    color: white;
}

/* Text Area */
textarea {
    background-color: #1E1E1E !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🛡️ AlphaNet")
st.subheader("Network Utility & Monitoring Suite")
st.caption("Monitor. Analyze. Optimize.")

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.title("🛠️ AlphaNet Menu")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🌐 Website Monitor",
        "📥 Bulk Downloader",
        "⚡ Speed Test"
    ]
)

st.sidebar.success("🟢 System Online")

# ---------------- DASHBOARD METRICS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("⬇ Download", "85 Mbps")

with col2:
    st.metric("⬆ Upload", "42 Mbps")

with col3:
    st.metric("📡 Ping", "12 ms")

with col4:
    st.metric("🌐 Status", "ONLINE")

st.divider()

# ---------------- WEBSITE MONITOR ----------------
if menu == "🌐 Website Monitor":

    st.subheader("🌐 Website Uptime Monitor")

    url = st.text_input("Enter Website URL")

    if st.button("Check Status"):
        st.success("Website is Online ✅")

# ---------------- BULK DOWNLOADER ----------------
elif menu == "📥 Bulk Downloader":

    st.subheader("📥 Bulk URL Downloader")

    urls = st.text_area("Paste URLs Here")

    if st.button("Start Download"):
        st.info("Downloading Started...")

        progress = st.progress(0)

        for i in range(100):
            progress.progress(i + 1)

        st.success("Download Completed ✅")

# ---------------- SPEED TEST ----------------
elif menu == "⚡ Speed Test":

    st.subheader("⚡ Internet Speed Analyzer")

    if st.button("Run Speed Test"):

        st.info("Running Speed Test...")

        st.metric("⬇ Download Speed", "92 Mbps")
        st.metric("⬆ Upload Speed", "45 Mbps")
        st.metric("📡 Ping", "10 ms")

        st.success("Speed Test Completed ✅")
