#Standard Libraries
import ast 
import io
from tempfile import NamedTemporaryFile

# Third-Party Libraries
from PIL import Image
import streamlit as st 

# Imported Libraries
from backend import analyze_image, file_to_data_url

def custom_container(background_color: str, 
                     content: str):
    
    # Define a container with a background color
    container_style = f"""
    <div style="background-color:{background_color}; 
    color: #f5f5f5;
    text-shadow: 1.5px 1.5px 2px black,
    1.2px 1.2px 2px black;
    letter-spacing: 5px;
    margin: 3px; 
    border-radius:10px;
    border: 5px solid #d3d3d3;
    font-size: 21px;
       ">
        {content}
    </div>
    """
    # Use st.markdown to render the customized container
    st.markdown(container_style, unsafe_allow_html=True)

st.set_page_config(layout="wide", 
                   page_title="Hex Color Code Identifier")

st.header("**:blue-background[Hex Number Identifier]**")
st.markdown('''The hex color code finder given an image. 
            Please upload an image from your local computer and 
            put in your Hugging Face API Token in order to 
            start the process below. Press start when 
            both fields has been filled.
            \nThe five most common hex color codes 
            found in the image will be displayed. 
            ''')
st.link_button(label="Source Code Found Here", url="https://github.com/nerutoki/HexIdentifier",
               type = "secondary")

col1, col2 = st.columns(spec = [4,6], gap = "small", 
                        vertical_alignment="top", 
                        border = False)

with col2:
    st.markdown("### :red-background[Hugging Face API Token]")

    st.markdown('''Please provide Hugging Face API Token. 
                  Token will not be saved after closing page. Instructions
                  on creating a Hugging Face API Token can be found below.
                  Please ask permission from Llama-3.2-11B-Vision-Instruct
                on Hugging Face in order to use this website. Access to model
                can be found below.''')

    HF_api_key = st.text_input(label=''' # **Hugging Face Account required.**
                  ''', type="password", placeholder="Token Here")
    
   
    col3, col4 = st.columns(2, gap="small")

    col3.link_button(label="Llama-3.2-11B-Vision-Instruct", url="https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct",
                     type = "secondary")
    col4.link_button(label = "Create Hugging Face API Token", url="https://huggingface.co/docs/hub/en/security-tokens",
                     type = "secondary")
    
    st.markdown(''' If Hugging Face API Token is not inputted correctly,
                the website will not be able to proceed with your request.
                If file was inputted correctly, please check your 
                Key.
                ''')
    st.markdown("### :red-background[Original Image]")

with col1:

    st.markdown(''' 
                ### :red-background[Upload File Below]''')
    st.markdown('''Please upload an image from local computer.
                Data is not stored on this website.
                \nThe process can be repeated by 
                uploading a new image.
                \n Accepted Files: 
                \n- .jpg
                \n- .png
                ''')

    uploaded_file = st.file_uploader(label = "File", type=['png', 'jpg'],
                                     accept_multiple_files=False,
                                     label_visibility="collapsed")

    if st.button("Start", type = 'primary'):

        if uploaded_file == None:
            if uploaded_file == None:
                st.markdown("File is not in the proper extension. Please try again.")
      
        elif uploaded_file != None and (HF_api_key != None or HF_api_key != ""):
            buffer = io.BytesIO()
            temp_result = None

            resize_image = Image.open(uploaded_file)

            if resize_image.format == "PNG":
                resize_image = resize_image.resize((256,256))
                resize_image.save(buffer, format='PNG')

                with NamedTemporaryFile(dir='.', suffix='PNG') as f:
                    f.write(buffer.getbuffer())
                    image_url = file_to_data_url(f.name)

                temp_result = image_url
            elif resize_image.format == "JPEG":
                resize_image = resize_image.resize((256,256))
                resize_image.save(buffer, format='JPEG', quality=75)

                with NamedTemporaryFile(dir='.', suffix='JPEG') as f:
                    f.write(buffer.getbuffer())
                    image_url = file_to_data_url(f.name)

                temp_result = image_url

            prompt = """
            Analyze the following image for all the hex values. Return all the hex values
            in the following format: {"#C7700F": "Light Green"}. 
            Here are the rules:
            1) Make sure all hex numbers and colors are valid.
            2) Only use valid unicode for Python.
            3) Make sure the output is only one dictionary.
            4) Output only 5 of the most common hex numbers in the image.
            Make sure to only output a valid Python dictionary and nothing else.
            Output a valid Python dictionary.
            """

            response = analyze_image(prompt = prompt, 
                                    image_url = temp_result,
                                    HF_api_key = HF_api_key)

            
            #convert dictionary string to dictionary
            res = ast.literal_eval(response)
            
            st.markdown(''' 
                        ### :red-background[Hex Number and Colors]''')

            color_dict_keys = []
            color_dict_values = []

            for key,val in res.items():
                color_dict_keys.append(key)
                color_dict_values.append(val)

            counter = 0
            
            for col in range(0, len(color_dict_keys)):
                st.markdown(f"#### :blue-background[{str(color_dict_values[counter])}]")
                custom_container(color_dict_keys[counter], str(color_dict_keys[counter]))
                counter = counter + 1

                if counter > len(res)-1:
                    break
    else:
        st.stop()

    if uploaded_file == None:
        with col2:
            st.empty()
    else:
        with col2:
            image = Image.open(uploaded_file)
            st.image(image = image)

    
