#Standard Libraries
import ast 
from tempfile import NamedTemporaryFile


# Third-Party Libraries
from PIL import Image
import streamlit as st 


# Imported Libraries
from backend import analyze_image, file_to_data_url

def custom_container(background_color: str, content: str):
    # Define a container with a background color
    container_style = f"""
    <div style="background-color:{background_color}; padding: 20px; border-radius: 8px;">
        {content}
    </div>
    """
    
    # Use st.markdown to render the styled container
    st.markdown(container_style, unsafe_allow_html=True)



st.header("Hex Number Identifier")

st.markdown("Please add a valid image from your local machine.")
uploaded_file = st.file_uploader("File Upload", type=['png','jpg'])

if uploaded_file != None:
    with NamedTemporaryFile(dir='.', suffix='.png') as f:
        f.write(uploaded_file.getbuffer())
        image_url = file_to_data_url(f.name)

        temp_result = image_url

    st.markdown("# Original Image")
    image = Image.open(uploaded_file)
    st.image(image = image)

    prompt = """
    Analyze the following image for all the hex values. Return all the hex values
    in the following format: {"#C7700F": "green"}. 
    Here are the rules:
    1) Make sure all hex numbers are valid.
    2) Only use valid unicode for Python.
    3) Make sure the output is only one dictionary.
    4) Output only 5 of the most common hex numbers in the image.
    Make sure to only output a valid Python dictionary and nothing else.
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

    st.markdown("# Extracted Hex Number and Colors")
    st.markdown("Below you can find the extracted Hex Numbers and their associated colors taken from the image above.")

    colors_rows = [x for x in range(0,10)]
    colors_grid_test = []

    for x in range(0,10):
        colors_rows[x] = st.columns(5)
        colors_grid_test = colors_grid_test + (colors_rows[x])

    color_dict_keys = []
    color_dict_values = []

    for key,val in res.items():
        color_dict_keys.append(key)
        color_dict_values.append(val)

    counter = 0

    for col in colors_grid_test:
        custom_container(color_dict_keys[counter], str(color_dict_keys[counter]) + " " + color_dict_values[counter])
        counter = counter + 1

        if counter > len(res)-1:
            break