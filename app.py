# import streamlit as st # type: ignore
# from pathlib import Path

# st.set_page_config(page_title="Traffic Detection", layout="wide")

# st.title("🚦 Lagos Traffic Detection (YOLOv8)")

# video_path = Path("output.mp4")

# if not video_path.exists():
#     st.error("Processed video not found.")
# else:
#     st.success("Processed video loaded")
#     st.video(str(video_path))

import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

st.title("🚦 Traffic monitoring using object detection (YOLOv8)")

video_path = Path("output.mp4")

if not video_path.exists():
    st.error("Processed video not found.")
else:
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.video(str(video_path))

