import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Set the title of your Streamlit app
st.title("Deepfake Detector App")

# Choose between image and video upload
file_type = st.radio("Select file type:", ("Image", "Video"))

# Upload file through Streamlit

uploaded_file = st.file_uploader(f"Choose a {file_type.lower()}...", type=[
        "jpg", "jpeg", "png", "mp4"])


# Display the uploaded file
if uploaded_file is not None:
    if file_type == "Image":
        # Display the uploaded image
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", width=200)
        except Exception as e:
            st.error(f"Error: Invalid Filetype")
    else:
        st.video(uploaded_file)

    # Check if the user wants to perform the deepfake detection
    if st.button("Check for Deepfake"):
        # Convert file to bytes for API request
        file_bytes = BytesIO()
        if file_type == "Image":
            uploaded_file.seek(0)
            file_bytes.write(uploaded_file.read())
            # Replace with your Flask image API endpoint
            api_url = "http://127.0.0.1:5000/process_image"
            files = {"image": (f"{file_type.lower()}.jpg",
                               file_bytes.getvalue(), "image/jpeg")}
        else:
            file_bytes.write(uploaded_file.read())
            # Replace with your Flask video API endpoint
            api_url = "http://127.0.0.1:5000/process_video"
            files = {"video": (f"{file_type.lower()}.mp4",
                               file_bytes.getvalue(), "video/mp4")}
        # Make a POST request to your Flask API

        response = requests.post(api_url, files=files)

        # Display the result
        if response.status_code == 200:
            result = response.json()["output"]
            if result == "real":
                st.success(f"This {file_type.lower()} is real!")
            else:
                st.error(f"This {file_type.lower()} is fake!")
        else:
            st.error("Error: Something went wrong...Try using different file format.")
else:
    st.info("Please upload a file.")

# Add additional information or description about your project
st.markdown(
    """
    ## Project Information
    This Streamlit app uses a Flask API to detect deepfake images and videos. 
    The deepfake detection is performed by sending the uploaded file to the Flask API, 
    which then returns the result.

    Feel free to customize the UI and styling based on your preferences.
    """
)
