#Standard Libraries
import ast 
from tempfile import NamedTemporaryFile


# Third-Party Libraries
import streamlit as st 

# Imported Libraries
from backend import analyze_image, file_to_data_url

temp_result = ""

uploaded_file = st.file_uploader("File upload", type='png')

if uploaded_file != None:
    with NamedTemporaryFile(dir='.', suffix='.png') as f:
        f.write(uploaded_file.getbuffer())
        image_url = file_to_data_url(f.name)

        temp_result = image_url

    prompt = """
    Give me a valid python dictionary where each key and value needs double quotes
    around it. Make the key be a hex number and value be a color found in the 
    image. Only output a python dictionary.
    """

    response = analyze_image(
        prompt = prompt, image_url = temp_result
    )

    # using ast.literal_eval()
    # convert dictionary string to dictionary
    res = ast.literal_eval(response)

        # print result
    # print("The converted dictionary : " + str(res))

    st.markdown(str(res))