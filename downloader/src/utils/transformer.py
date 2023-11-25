"""Transform the metadata into a list of videos."""
def build_list_of_videos_mp4(metadata: list) -> list:
    """Build a list of MP4 video files from the metadata.

    Args:
        metadata (list): The metadata for the files.

    Returns:
        list: A list of dictionaries, each representing a video file.
    """
    video_list = []
    for file in metadata:
        if file['name'].endswith('.mp4'):
            video = {'name': file['name'], 'size': int(file['size'])}
            video_list.append(video)
    return video_list

def build_list_of_videos_mkv(metadata: list) -> list:
    """Build a list of MKV video files from the metadata.

    Args:
        metadata (list): The metadata for the files.

    Returns:
        list: A list of dictionaries, each representing a video file.
    """
    video_list = []
    for file in metadata:
        if file['name'].endswith('.mkv'):
            video = {'name': file['name'], 'size': int(file['size'])}
            video_list.append(video)
    return video_list