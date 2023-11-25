import os
import httpx
from tqdm import tqdm
from loguru import logger

def file_exists(filename: str, save_folder: str) -> bool:
    """Check if a file already exists in the save folder."""
    full_path = os.path.join(save_folder, filename)
    return os.path.isfile(full_path)

def download_file(url: str, filename: str, save_folder: str) -> None:
    """Download a file from a URL."""
    if file_exists(filename, save_folder):
        logger.info(f"File {filename} already exists in {save_folder}. Skipping download.")
        return

    file_url = os.path.join(url, filename)
    # Log the file download initiation
    logger.info(f"Starting download of {filename} from {url}")
    timeout = httpx.Timeout(10.0, read=60.0)  # 10s connect timeout, 60s read timeout
    with httpx.Client(timeout=timeout) as client:
        # Stream the response
        with client.stream("GET", file_url, follow_redirects=True) as response:
            response.raise_for_status()  # Check response status within the client context
            total_size = int(response.headers.get('content-length', 0))

            full_path = os.path.join(save_folder, filename)

            with open(full_path, 'wb') as fd, tqdm(total=total_size, unit='iB', unit_scale=True) as progress_bar:
                for chunk in response.iter_bytes(chunk_size=1024 * 1024):  # Chunk size of 1MB
                    fd.write(chunk)
                    progress_bar.update(len(chunk))

    logger.info(f"Downloaded {filename} to {save_folder}")
