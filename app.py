import streamlit as st
import requests
import time
import os
import speedtest

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AlphaNet",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
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

/* Text Inputs */
.stTextInput > div > div > input {
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

# =========================================================
# HEADER
# =========================================================
st.title("🛡️ AlphaNet")
st.subheader("Network Utility & Monitoring Suite")
st.caption("Monitor. Analyze. Optimize.")

st.divider()

# =========================================================
# SIDEBAR
# =========================================================
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

# =========================================================
# TOP METRICS
# =========================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("⬇ Download", "LIVE")

with col2:
    st.metric("⬆ Upload", "LIVE")

with col3:
    st.metric("📡 Ping", "LIVE")

with col4:
    st.metric("🌐 Status", "ACTIVE")

st.divider()

# =========================================================
# WEBSITE MONITOR
# =========================================================
if menu == "🌐 Website Monitor":

    st.subheader("🌐 Website Uptime Monitor")

    url = st.text_input(
        "Enter Website URL",
        placeholder="https://google.com"
    )

    if st.button("Check Website Status"):

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
                        "🟢 Server Status",
                        "ONLINE"
                    )

                st.divider()

                if response.status_code == 200:

                    st.success("✅ Website is ONLINE")

                    st.balloons()

                else:

                    st.warning(
                        "⚠️ Website reachable but returned an issue"
                    )

            except Exception as e:

                st.error("❌ Website is OFFLINE or invalid URL")

                st.code(str(e))

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

    download_folder = "downloads"

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    if st.button("Start Download"):

        if urls:

            url_list = urls.splitlines()

            progress_bar = st.progress(0)

            downloaded_files = []

            for index, url in enumerate(url_list):

                url = url.strip()

                if url:

                    try:

                        response = requests.get(url)

                        if response.status_code == 200:

                            filename = url.split("/")[-1]

                            if filename == "":
                                filename = f"file_{index}"

                            file_path = os.path.join(
                                download_folder,
                                filename
                            )

                            with open(file_path, "wb") as file:
                                file.write(response.content)

                            downloaded_files.append(file_path)

                            progress_bar.progress(
                                (index + 1) / len(url_list)
                            )

                        else:

                            st.error(
                                f"❌ Failed to download: {url}"
                            )

                    except Exception as e:

                        st.error(f"❌ Error downloading: {url}")

                        st.code(str(e))

            st.success(
                f"✅ Successfully downloaded {len(downloaded_files)} files"
            )

            st.divider()

            st.subheader("📂 Downloaded Files")

            for file_path in downloaded_files:

                file_name = os.path.basename(file_path)

                st.write(f"✅ {file_name}")

                with open(file_path, "rb") as file:

                    st.download_button(
                        label=f"⬇ Save {file_name}",
                        data=file,
                        file_name=file_name,
                        mime="application/octet-stream"
                    )

        else:

            st.warning("⚠️ Please paste at least one URL")

# =========================================================
# SPEED TEST
# =========================================================
elif menu == "⚡ Speed Test":

    st.subheader("⚡ Real-Time Internet Speed Test")

    st.info("Run a real network speed analysis")

    if st.button("Run Speed Test"):

        try:

            with st.spinner("Running Speed Test..."):

                progress = st.progress(0)

                for i in range(30):
                    time.sleep(0.03)
                    progress.progress((i + 1) * 3)

                # Initialize Speed Test
                stest = speedtest.Speedtest()

                # Find Best Server
                stest.get_best_server()

                # Run Tests
                download_speed = stest.download() / 1_000_000
                upload_speed = stest.upload() / 1_000_000
                ping_result = stest.results.ping

                progress.progress(100)

            st.success("✅ Speed Test Completed Successfully")

            st.divider()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "⬇ Download Speed",
                    f"{download_speed:.2f} Mbps"
                )

            with col2:
                st.metric(
                    "⬆ Upload Speed",
                    f"{upload_speed:.2f} Mbps"
                )

            with col3:
                st.metric(
                    "📡 Ping",
                    f"{ping_result:.2f} ms"
                )

            st.divider()

            # Connection Quality
            if download_speed > 100:

                st.success(
                    "🚀 Excellent Internet Connection"
                )

            elif download_speed > 50:

                st.info(
                    "⚡ Good Internet Connection"
                )

            else:

                st.warning(
                    "🐢 Slow Internet Connection"
                )

            st.balloons()

        except Exception as e:

            st.error("❌ Speed Test Failed")

            st.code(str(e))

# =========================================================
# FOOTER
# =========================================================
st.divider()

st.caption(
    "🛡️ AlphaNet | Developed by Team ALPHA PAIR"
)
