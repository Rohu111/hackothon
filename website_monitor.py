import streamlit as st
import requests
import time

st.set_page_config(
    page_title="Website Monitor | AlphaNet",
    page_icon="🌐",
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
# WEBSITE MONITOR
# =========================================================
st.title("🌐 Website Uptime Monitor")

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
