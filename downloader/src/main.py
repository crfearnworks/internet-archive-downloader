from utils.downloader import download_file
from utils.metadata import get_metadata, filter_mp4_files, filter_mkv_files
from config import BASE_URL
import requests

if __name__ == "__main__":

    
    item_id = "your_item_id_here"
    item_url = f"{BASE_URL}/{item_id}/"
    filter_text = "your_filter_text_here"

    try:
        metadata = get_metadata(item_id)
        mp4_files = filter_mp4_files(metadata, filter_text)
        mk4_files = filter_mkv_files(metadata, filter_text)

        for i, file in enumerate(mp4_files, start=1):
            file_name = file['name']
            url = BASE_URL + file_name
            download_file(url, file_name)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")    

    # need a chooser here for mp4 or mkv
    # then need to download the file
    # then need to convert the file
    # then need to delete the file
    # then need to move on to the next file

    # need to add a progress bar
    # need to add a timer
    # need to add a counter
    # need to add a file size
    # need to add a file name
    # need to add a file type
    # need to add a file path
    # need to add a file duration



        
        
            
