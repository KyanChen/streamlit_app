import pre_reqs
import streamlit as st
# https://huggingface.co/spaces/KyanChen/ai-photo-gallery

# streamlit run app.py --server.port 9001


st.set_page_config(
    page_title="AI photo Gallery",
    page_icon="👋",
)

st.write("# AI Photo Gallery 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    AI Photo Gallery 👋！
    """
)