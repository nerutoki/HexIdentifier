# Hex Identifier
Identifies and return the five most common hex color codes in an image given by the user. It uses the Large Language Model, **Meta Llama-3.2-11B-Vision-Instruct** to identifies the hex color codes. Hugging Face's account is required.

![Website Interface](https://github.com/nerutoki/HexIdentifier/blob/main/hexIdentifier_website_page.png?raw=true)

# Getting Started

## Prerequisites

## Installing

1) Create an virtual environment in your terminal.
    ```
    $ python3 -m venv env 
    $ source env/bin/activate
    ```

2) Clone the repo
   ```sh
    git clone https://github.com/nerutoki/HexIdentifier.git
    ```

3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

4)
    Install the required packages.
    ```
    $ pip install uv
    ```

    ```
    $ uv pip compile requirements.txt
    ```

## Run 

Run the code below in your terminal.
```
$ streamlit run streamlit_app.py
```

## Usage

### Prerequisites
1) Create a Free API Key at [Hugging Face](https://huggingface.co/)
2) Have a PNG or JPEG/JPG image in your local machine.

### Run

1) Attach your image to the file uploader. If the image is not a PNG or JPEG/JPG, it will not run.

2) Enter your Hugging Face API Key.

3) Click Start when both fields are filled. If program fail to start, please check if both fields were filled correctly.


## Resources
- Sample images is from https://www.pexels.com/photo/concrete-road-between-trees-1563356/ 
- file_to_data_url function is from https://huggingface.co/mistralai/Pixtral-12B-2409/discussions/6


