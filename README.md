# YouTube Video Downloader

This Python script provides a simple graphical user interface (GUI) to download YouTube videos, including audio and captions.

## Features

- Download the highest resolution video with audio.
- Download audio only.
- Download captions in a specified language.

## Requirements

- Python 3.x
- `pytube` library
- `youtube-transcript-api` library
- `tkinter` library (part of the Python standard library)

## Installation

1. Clone this repository or download the script.

2. Navigate to the directory containing the script.

3. Install the required libraries using the following command:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```sh
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of the Python script.

2. The GUI will appear. Enter the YouTube video URL, select options for downloading captions, and specify the output directory.

3. Click the "Download" button to start the download process.

## Example

1. Enter the YouTube URL:
    ```
    https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ```

2. Specify the language for captions (default is `en` for English).

3. Check the box if you want to download captions.

4. Select the output directory where you want to save the downloaded files.

5. Click "Download" and wait for the process to complete.

## Notes

- Ensure you comply with YouTube's terms of service when downloading content.
- The script may not work for videos that are restricted or have disabled captions.

## License

This project is distributed under a MODIFIED CREATIVE COMMONS ATTRIBUTION-NONCOMMERCIAL 3.0 LICENSE. Refer to the LICENSE file for specifics.