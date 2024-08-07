import pandas as pd
from my_functions import to_seconds

# represents the path where we wrote our video details into
# using the same variable name from youtwo.py
video_data = D:/Users/csv file path/to store/video details"

print("Hello, to use, you'll be asked how long you want the video to be ")
print()

min_minutes = to_seconds(int(input(
    "Enter the minimum number of minutes for the video you want to watch\n i.e 5 representing 5 minutes"
    "\n please enter only the number ")))
max_minutes = to_seconds(
    int(input("Enter the max number of minutes per video ")))


# filter time
df = pd.read_csv(video_data)
filtered_df = df[(df["duration"] >= min_minutes) &
                 (df["duration"] <= max_minutes)]
# this creates a custom column/data frame where the videos in that
# column are within the users preferred range

# to achieve the ultimate goal we want to provide the most popular videos within that range
filtered_df = filtered_df.sort_values(by="viewCount", ascending=False)
# we sort the videos  by viewCount with the highest coming first and descending

top_10_videos = filtered_df.head(10)

# Retrieve the video IDs of the top 10 most popular videos
top_10_video_ids = top_10_videos['id'].tolist()


# Retrieve the video ID of the most popular video
# print("the most popular video within your prefered range can be accessed with the link: https://youtu.be/{}".format(video_id))
print("The top 10 most popular videos within the specified range can be accessed with the links below")
print()
for i in top_10_video_ids:
    print("https://youtu.be/{}".format(i))
