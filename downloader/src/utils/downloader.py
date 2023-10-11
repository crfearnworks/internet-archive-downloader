import requests
from tqdm import tqdm
from typing import List, Dict

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
