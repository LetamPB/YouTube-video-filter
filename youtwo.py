from youtube import video_ids
from youtube import video_details
import csv

## Brief overview ###
# This script centers on effectively writing the details for each video
# into my csv file for easier analysis using the csv module and eventually panda


# file path where the details for each video will be stored
video_data = "D:/Users/csv file path/to store/video details"

with open(video_data, "w") as csv_file:
    fields = ["id", "duration", "viewCount"]
    # column headings of csv file to be written on the file
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields)

    csv_writer.writeheader()
    for item in video_details:
        csv_writer.writerow(item)
        # writes each ditionary entry from video details into

# data has been successfully written into csv file next step is
# filtering them based on duration
