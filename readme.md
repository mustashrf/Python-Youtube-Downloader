# Python-Youtube-Downloader

This is a command-line program that allows you to download videos or playlists from YouTube using pytube library.


## How to use

1. Run the program using the following command: 
`python youtube_downloader.py`


2. Choose the download type:
- `s` for single video
- `p` for playlist
- `f` to provide a file with URLs
- `q` to quit the process

3. If you choose `s` or `p`, the program will ask for:
    - Number of trials (iterations).
    - URL of the video or playlist you want to download.
    - If it's a playlist, you can optionally specify exceptions for videos not to be downloaded. For example, enter `1,2,3-7,9` to skip videos 1, 2, 3 to 7, and 9.
    - Optinally specify where to download.
    - Choose to download it as a video or audio only (1 or 0) respectively.
    - Quality (360 or 720) in the video case.

4. If you choose `f`, you need to provide a file with download instructions in the following format:
     ```
     p
    https://www.youtube.com/XXXXXXXX
    download-path/
    1 (video or audio)
    720

    s
    https://www.youtube.com/XXXXXXXX
    download-path/
    1
    720
     ```

5. Any download failures will be printed out after the process is completed.

6. After the download process is completed, a system beep will be emitted to notify the user.


## Dependencies

- Python 3
- pytube

## Installation

  - Install pytube library using pip:
    `pip install pytube`
  - Download the `YoutubeDownloader.py` file from this repository.
  - Run: `python YoutubeDownloader.py` (windows) or `python3 YoutubeDownloader.py` (linux).

