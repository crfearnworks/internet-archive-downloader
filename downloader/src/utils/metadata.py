import json
import requests
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