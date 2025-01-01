# Standard Libraries
import ast
import base64
import json
import os

# Third-Party Libraries
from huggingface_hub import InferenceClient

def file_to_data_url(file_path: str):
    """
    Convert a local image file to a data URL.
    """    
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    _, extension = os.path.splitext(file_path)
    mime_type = f"image/{extension[1:].lower()}"
    
    return f"data:{mime_type};base64,{encoded_string}"


def analyze_image(prompt, image_url, HF_api_key):
    """ Take the hex number of the colors found in the given image.

    Args:
        prompt (str): Prompt the LLM
        image_url (str): Location of image from web

    Return: 
        response (str): Answer from LLM

    """
    
    api_key = HF_api_key

    client = InferenceClient(api_key= api_key)

    messages = [
        {
            "role": "user",
            "content": 
            [
                {
                    "type": "text",
                    "text": prompt
                },

                {
                    "type": "image_url",
                    "image_url": 
                    {
                        "url": image_url
                    }
                }
            ]
        }
    ]

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct", 
        messages=messages, 
        max_tokens=500
    )

    response = completion.choices[0].message.content

    return response
    


if __name__ == "__main__":

    image_local_path = "sample_input_1.jpg"
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
    
    image_url = file_to_data_url(image_local_path)
    
    response = analyze_image(
        prompt = prompt, image_url = image_url
    )

    # convert dictionary string to dictionary
    res = ast.literal_eval(response)

    # print result
    print("The converted dictionary : " + str(res))