import re
# Adapted from code provided by Corey Shafer on GitHub
#source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/YouTube-API/02-Playlist-Duration/playlist.py
def iso_duration_to_seconds(duration):
    """
    Converts an ISO duration string to seconds.

    Args:
        duration (str): ISO duration string (e.g., "PT3M35S" for 3 minutes and 35 seconds).

    Returns:
        int: Total duration in seconds.
    """
    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    seconds_pattern = re.compile(r'(\d+)S')

    hours = hours_pattern.search(duration)
    minutes = minutes_pattern.search(duration)
    seconds = seconds_pattern.search(duration)

    hours = int(hours.group(1)) if hours else 0
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1)) if seconds else 0

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def to_seconds(values):
    """
    Converts time received in minutes to seconds.

    Args:
        values (int): The time in minutes. e.g 10 for 10 minutes.

    Returns:
        int: Total duration  converted to seconds.

    Raises:
        ValueError: if the input entered by user exceeds 60(up to an hour)
        or if the user enters anything that is not an integer
    """
    if values > 60 or type(values) != int:
        raise ValueError("the time range can only be in minutes")
    else:
        minutes = values*60
        return minutes
