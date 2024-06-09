import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


def download_youtube_video():
    url = url_entry.get()
    output_path = filedialog.askdirectory()
    download_captions = captions_var.get()
    language = language_entry.get()

    if not url or not output_path:
        messagebox.showerror("Error", "Please provide a valid URL and output path.")
        return

    try:
        # Create YouTube object
        yt = YouTube(url)

        # Download the highest resolution video
        video_stream = (
            yt.streams.filter(progressive=True, file_extension="mp4")
            .order_by("resolution")
            .desc()
            .first()
        )
        video_stream.download(output_path)

        # Download the audio
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        audio_stream.download(
            output_path,
            filename=audio_stream.default_filename.replace(".mp4", "_audio.mp4"),
        )

        # Download captions if requested
        if download_captions:
            try:
                captions = YouTubeTranscriptApi.get_transcript(
                    yt.video_id, languages=[language]
                )
                with open(
                    f"{output_path}/{yt.title}_captions_{language}.srt",
                    "w",
                    encoding="utf-8",
                ) as f:
                    for caption in captions:
                        f.write(f"{caption['start']}\n{caption['text']}\n\n")
            except Exception as e:
                messagebox.showerror("Error", f"Could not download captions: {e}")
                return

        messagebox.showinfo("Success", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place the widgets
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Language for Captions:").grid(row=1, column=0, padx=10, pady=5)
language_entry = tk.Entry(root, width=10)
language_entry.grid(row=1, column=1, padx=10, pady=5)
language_entry.insert(0, "en")  # Default language

captions_var = tk.BooleanVar()
captions_check = tk.Checkbutton(root, text="Download Captions?", variable=captions_var)
captions_check.grid(row=2, columnspan=2, padx=10, pady=5)

is_short_var = tk.BooleanVar()
is_short_check = tk.Checkbutton(root, text="Is Video a Short?", variable=is_short_var)
is_short_check.grid(row=3, columnspan=2, padx=10, pady=10)

download_button = tk.Button(root, text="Download", command=download_youtube_video)
download_button.grid(row=4, columnspan=2, pady=15)

# Start the main event loop
root.mainloop()
