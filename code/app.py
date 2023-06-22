import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimg

# Function to apply the desired filters
"""
We have 3 kinds of filters: 'Grayscale, Invert and Blur'
"""
def apply_filter(image, filter_type):
    if filter_type == "Grayscale":
        return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    elif filter_type == "Invert":
        return 1 - image
    elif filter_type == "Blur":
        kernel = np.ones((5,5)) / 25.0
        return np.convolve2d(image, kernel, mode='same')
    else:
        return image
    

def main():
    st.title("Image Filter Application")

    file_uploader = st.file_uploader("Upload an Image", type=["png", "jpeg", "jpg"])
    filter_options = st.selection("Select a Filter", ["None", "Grayscale", "Invert", "Blur"])


    if file_uploader is not None:

        image = mimg.imread(file_uploader)

        filtered_image = apply_filter(image, filter_options)

        st.header("Original Image")
        st.image(image, use_column_width=True)




if __name__ == "__main__":
    main()
