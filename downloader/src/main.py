import os
from dotenv import load_dotenv
from loguru import logger
from utils.parse_web_page import get_url_from_user, get_metadata
from utils.transformer import build_list_of_videos_mkv, build_list_of_videos_mp4
from utils.downloader import download_file

load_dotenv()

ARCHIVE_FOLDER = os.getenv("ARCHIVE_PATH")

def archiver_pipeline():
    """Download files pipeline from the Internet Archive."""
    archive_url = get_url_from_user()
    metadata = get_metadata(archive_url)
    if any(file['name'].endswith('.mkv') for file in metadata):
        video_list = build_list_of_videos_mkv(metadata)
    elif any(file['name'].endswith('.mp4') for file in metadata):
        video_list = build_list_of_videos_mp4(metadata)
    else:
        raise ValueError("No downloadable videos exist in the provided metadata.")

    for video in video_list:
        download_file(archive_url, video['name'], ARCHIVE_FOLDER)

if __name__ == "__main__":
    archiver_pipeline()
