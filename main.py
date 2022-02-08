# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np



def load_image(image_file):
    img = Image.open(image_file)
    return img



angle =0

def get_augs(image_file,width,height):
    img=  load_image(image_file)
    agl = st.slider('Do you want to Rotate the Image', -180, +180, value=0, step=1)
    img = img.rotate(agl)
    angle = agl
    st.image(img , width = 250)
    print(agl)
    return  agl

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    st.title('Bone Age Estimation ')
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
    option = st.radio('Sex', ['Male', 'Female'])
    #image_file_picture = st.camera_input("Take a picture")


    if image_file is not None:
        # To See details
        img = load_image(image_file)
        width, height = img.size
        st.subheader('Align the Image')
        angle = get_augs(image_file,width,height)





    if st.button('Get Results'):
        if option is not None and image_file is not None:
            file_details = {"filename": image_file.name, "filetype": image_file.type,
                            "filesize": image_file.size,
                            "Height": height,
                            "Width": width,
                            "Sex": option,
                            "aug" : angle
                            }
            st.write(file_details)
            # To View Uploaded Image
            # st.image(load_image(image_file), width=width)
            # col1, col2, col3 = st.columns([0.5, 2, 0.5])
            # col1.write(file_details)
            # col2.image(img)
            # st.write("I'm ", age, 'years old')
        elif image_file is None:
            st.write('Please select Image first')
        elif option is None:
            st.write('Please select Sex first')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
