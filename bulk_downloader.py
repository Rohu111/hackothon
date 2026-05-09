import streamlit as st
import requests
import os

st.set_page_config(
    page_title="Bulk Downloader | AlphaNet",
    page_icon="📥",
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
# BULK DOWNLOADER
# =========================================================
st.title("📥 Bulk URL Downloader")

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

        status_box = st.empty()

        for index, url in enumerate(url_list):

            url = url.strip()

            if url:

                try:

                    status_box.info(
                        f"⬇ Downloading: {url}"
                    )

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

                    st.error(
                        f"❌ Error downloading: {url}"
                    )

                    st.code(str(e))

        status_box.success(
            "✅ Download Process Completed"
        )

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
