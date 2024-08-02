from googleapiclient.discovery import build
from my_functions import iso_duration_to_seconds
import csv

## Brief overview ###
# This script is used to to obtain details about evry video on my watch later playlist.
# The details obtained will form the backbone of how the choice of video automation will be made
# when attempting to replicate this preferably create a virtual environment


# Put in your personal API key into the variable below
api_key = "Enter your own API key"

# directory/file path for the content of vidoes in my watch later playlist
Watch_later_csv_file = "D:/Users/your/path/for your/watchlater/playlist/on/your computer"

youtube = build('youtube', 'v3', developerKey=api_key)

video_ids = []
with open(Watch_later_csv_file, newline="") as csv_file:
    csv_file_reader = csv.DictReader(csv_file)
    # represents the csv file being opened
    for row in csv_file_reader:
        video_ids.append(row["Video ID"])
        # within the csv file there's a row titled Video ID

    video_details = []
    # this is created to store the details for each video this will be
    # extracted via the API call below it will be a lists of dictionary
    # entries per video

    for i in range(0, len(video_ids), 50):
        batch_ids = video_ids[i:i+50]
        request = youtube.videos().list(
            part="contentDetails,statistics",
            id=','.join(batch_ids)
        )
        # because of the number of videos,the API call will happen in
        # batches of 50
        response = request.execute()
        # executes API call
        for item in response['items']:
            video_details.append({
                'id': item['id'],
                'duration': iso_duration_to_seconds(item['contentDetails']['duration']),
                # the duration is in an ISO_8601 format so we use Regex
                # to extract the exact time. i.e PT4M42S 4 minutes,42 seconds
                # the function will extract the time and convert to seconds
                'viewCount': item['statistics']['viewCount']
            })

# we focused on reducing the amount of API calls
# Hence the use of video_details to store the necessary information
# video details will be extracted to a CSV file for analysis

# API call done, no need to do it again.
# video_details has apporpriate things!
