import streamlit as st
import speedtest
import time

st.set_page_config(
    page_title="Speed Test | AlphaNet",
    page_icon="⚡",
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

div[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #00C8FF;
    padding: 15px;
    border-radius: 15px;
}

h1, h2, h3 {
    color: #00FF9F;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SPEED TEST
# =========================================================
st.title("⚡ Real-Time Internet Speed Test")

st.info("Run a real network speed analysis")

if st.button("Run Speed Test"):

    try:

        status_text = st.empty()

        progress = st.progress(0)

        # STEP 1
        status_text.info("🔍 Finding best server...")
        progress.progress(10)

        stest = speedtest.Speedtest()

        stest.get_best_server()

        time.sleep(1)

        # STEP 2
        status_text.info("⬇ Testing download speed...")
        progress.progress(35)

        download_speed = stest.download() / 1_000_000

        time.sleep(1)

        # STEP 3
        status_text.info("⬆ Testing upload speed...")
        progress.progress(70)

        upload_speed = stest.upload() / 1_000_000

        time.sleep(1)

        # STEP 4
        status_text.info("📡 Calculating ping...")
        progress.progress(90)

        ping_result = stest.results.ping

        time.sleep(1)

        # FINISH
        progress.progress(100)

        status_text.success(
            "✅ Speed Test Completed Successfully"
        )

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
