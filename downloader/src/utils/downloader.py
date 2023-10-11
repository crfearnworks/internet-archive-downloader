import json
import requests
from tqdm import tqdm
from typing import List, Dict

def get_metadata(item_id: str) -> Dict:
    """Fetch metadata from archive.org for a given item ID."""
    metadata_url = f"https://archive.org/metadata/{item_id}"
    response = requests.get(metadata_url)
    response.raise_for_status()
    return json.loads(response.text)

def filter_mp4_files(metadata: Dict, keyword: str) -> List[Dict]:
    """Filter out .mp4 files from metadata."""
    return [file for file in metadata['files'] if keyword in file['name'] and file['name'].endswith('.mp4')]

def filter_mkv_files(metadata: Dict, keyword: str) -> List[Dict]:
    """Filter out .mkv files from metadata."""
    return [file for file in metadata['files'] if keyword in file['name'] and file['name'].endswith('.mkv')]

def download_file(url: str, filename: str) -> None:
    """Download a file from a URL."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    
    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=1024):
            fd.write(chunk)
            progress_bar.update(len(chunk))

    progress_bar.close()
    print(f"Downloaded {filename}")

if __name__ == "__main__":
    item_id = "28-30dino-cosmic-fury-"
    base_url = f"https://archive.org/download/{item_id}/"

    try:
        metadata = get_metadata(item_id)
        mp4_files = filter_mp4_files(metadata, 'Cosmic Fury')
        
        for i, file in enumerate(mp4_files, start=1):
            file_name = file['name']
            url = base_url + file_name
            download_file(url, file_name)
            
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
