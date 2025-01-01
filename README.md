# Hex Identifier
Runs a website page that identifies and return the five most common hex color codes from an image given by the user. It uses the Large Language Model, **Meta Llama-3.2-11B-Vision-Instruct** to identifies the hex color codes. **Hugging Face's account is required.**

![Website Interface Example](https://github.com/nerutoki/HexIdentifier/blob/main/hexIdentifier_website_page.png?raw=true)

# Getting Started

## Prerequisites
This program uses Python 3.13.1.

## Installing

1) Create an virtual environment in your terminal.
    ```sh
    $ python3 -m venv env 
    $ source env/bin/activate
    ```

2) Clone the repository.
   ```sh
    $ git clone https://github.com/nerutoki/HexIdentifier.git
    ```

3. Change git remote url to avoid accidental pushes to base project
   ```sh
   $ git remote set-url origin github_username/repo_name
   $ git remote -v # confirm the changes
   ```

4)
    Install the required packages.
    ```sh
    $ pip install uv
    ```

    ```
    $ uv pip compile requirements.txt
    ```

### Run Locally

Run the code below in your terminal. A website page should appear shortly in your browser after executing the code.
```
$ streamlit run streamlit_app.py
```

## Usage of Website

### Prerequisites
1) Create a Free API Key at [Hugging Face](https://huggingface.co/)
2) Ask permission to usage of model  [Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct") on Hugging Face in order to use this website.
2) Prepare a PNG or JPEG/JPG image in your local machine.

### Run

1) Attach your image to the file uploader. If the image is not a PNG or JPEG/JPG file, it will not run.

![Uploading Image](https://github.com/nerutoki/HexIdentifier/blob/main/upload_file_example.png?raw=true)

2) Enter your Hugging Face API Key.

![Filling Out Hugging Face API Key Field](https://github.com/nerutoki/HexIdentifier/blob/main/fill_api_token_example.png?raw=true)

3) Click "Start" when both fields are filled. If program fail to start, please check if both fields were filled correctly.

![Conclusion of Filling Out Two Fields](https://github.com/nerutoki/HexIdentifier/blob/main/start_button_location.png?raw=True)

4) Example output.

![Output When Operation is Completed](https://github.com/nerutoki/HexIdentifier/blob/main/results_example.png?raw=True)


## Resources
- Sample image is from Craig Adderley at [Pexels](https://www.pexels.com/photo/concrete-road-between-trees-1563356/ )
- file_to_data_url function is from https://huggingface.co/mistralai/Pixtral-12B-2409/discussions/6
- The Large Language Model, [Meta Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) is used.
- LLM Model is accessed through [Hugging Face](https://huggingface.co/)