"""This module contains functions for parsing web pages."""
import json
import xml.etree.ElementTree as ET
import httpx

def get_url_from_user() -> str:
    """Get a URL from the user.

    Returns:
        str: A URL from the user.
    """
    url = input("Enter a URL from the Internet Archive: ")
    return url

def get_metadata(url: str) -> list:
    """Fetch metadata from archive.org for a given item ID.

    Args:
        url (str): The Internet Archive URL to fetch metadata for.

    Returns:
        list: The metadata of the files from the webpage.
    """

    item_id = url.split("/")[-1]
    files_xml_url = f"{url}/{item_id}_files.xml"
    with httpx.Client(follow_redirects=True) as client:
        response = client.get(files_xml_url)
    response.raise_for_status()
    root = ET.fromstring(response.text)
    # Now you can navigate the XML tree using the root element.
    metadata = []
    for file in root.findall('file'):
        file_data = {child.tag: child.text for child in file}
        file_data['name'] = file.get('name')  # Add the 'name' attribute of the 'file' element
        metadata.append(file_data)
    return metadata
