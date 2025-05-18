import streamlit as st

# Set page config
st.set_page_config(page_title="VinylScope", layout="centered")

# App Header
st.title("VinylScope - Scan Your Vinyl")
st.markdown(
    """
    **Upload photos of your vinyl record.**  
    We'll analyze the details and give you identity, value, and history insights.
    """
)

# File uploader
uploaded_files = st.file_uploader(
    "Upload up to 10 images (front/back cover, labels, matrix/runout, etc.)",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True,
    help="You can upload multiple images at once."
)

# Display uploaded images
if uploaded_files:
    st.subheader("Uploaded Images")
    for image in uploaded_files:
        st.image(image, caption=image.name, use_column_width=True)
