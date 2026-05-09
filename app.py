import streamlit as st
import requests
import time

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

/* Headers */
h1, h2, h3 {
    color: #00FF9F;
}

/* Buttons */
.stButton>button {
    background-color: #00C8FF;
    color: black;
    border-radius: 10px;
    font-weight: bold;
    width: 100%;
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

/* Labels */
label {
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

# ---------------- TOP METRICS ----------------
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

# =========================================================
# WEBSITE MONITOR
# =========================================================
if menu == "🌐 Website Monitor":

    st.subheader("🌐 Website Uptime Monitor")

    url = st.text_input(
        "Enter Website URL",
        placeholder="https://example.com"
    )

    if st.button("Check Status"):

        if url:

            try:
                start_time = time.time()

                response = requests.get(url, timeout=5)

                end_time = time.time()

                response_time = round(end_time - start_time, 2)

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "🌐 Status Code",
                        response.status_code
                    )

                with col2:
                    st.metric(
                        "⚡ Response Time",
                        f"{response_time} sec"
                    )

                with col3:
                    st.metric(
                        "🟢 Website",
                        "ONLINE"
                    )

                if response.status_code == 200:
                    st.success("✅ Website is ONLINE and reachable")
                    st.balloons()

                else:
                    st.warning(
                        "⚠️ Website reachable but returned an issue"
                    )

            except:
                st.error("❌ Website is OFFLINE or invalid URL")

        else:
            st.warning("⚠️ Please enter a valid URL")

# =========================================================
# BULK DOWNLOADER
# =========================================================
elif menu == "📥 Bulk Downloader":

    st.subheader("📥 Bulk URL Downloader")

    urls = st.text_area(
        "Paste URLs Here (One per line)",
        height=200
    )

    if st.button("Start Download"):

        if urls:

            url_list = urls.splitlines()

            total_urls = len(url_list)

            progress_bar = st.progress(0)

            status_text = st.empty()

            completed = 0

            for i, url in enumerate(url_list):

                if url.strip() != "":

                    status_text.info(f"Downloading: {url}")

                    time.sleep(0.5)

                    completed += 1

                    progress_bar.progress((i + 1) / total_urls)

            st.success(
                f"✅ Download simulation completed for {completed} URLs"
            )

        else:
            st.warning("⚠️ Please paste at least one URL")

# =========================================================
# SPEED TEST
# =========================================================
elif menu == "⚡ Speed Test":

    st.subheader("⚡ Internet Speed Analyzer")

    st.info(
        "Demo version for hackathon presentation"
    )

    if st.button("Run Speed Test"):

        with st.spinner("Running Speed Test..."):

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.02)
                progress.progress(i + 1)

        st.success("✅ Speed Test Completed")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "⬇ Download Speed",
                "92 Mbps"
            )

        with col2:
            st.metric(
                "⬆ Upload Speed",
                "45 Mbps"
            )

        with col3:
            st.metric(
                "📡 Ping",
                "10 ms"
            )

        st.balloons()

        st.info(
            "Network quality is stable and performing efficiently."
        )

# ---------------- FOOTER ----------------
st.divider()

st.caption(
    "🛡️ AlphaNet | Developed by Team ALPHA PAIR"
)
