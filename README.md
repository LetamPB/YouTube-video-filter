Key Features:
•	Extract video details from your "Watch Later" playlist.
•	Store video data in a CSV file for easy access.
•	Filter videos based on duration preferences.
•	Output a curated list of 10 YouTube video links.

Go through the 4 python scripts in this order:
youtube.py
youtwo.py
my_functions.py
final_script.py


Prerequisites
1. Google API Key Setup
Before running the scripts, you need to obtain a Google API key. Follow these steps:
1.	Go to the Google Developers Console.
2.	Create a new project.
3.	Enable the YouTube Data API v3.
4.	Create credentials:
o	Choose "Other non-UI" for the application type.
o	Select "Public data" for the access level.
5.	Copy the API key and store it securely.
2. Google Takeout
Since the YouTube API does not provide access to the "Watch Later" playlist, you'll need to use Google Takeout to export your playlist data.
1.	Visit Google Takeout.
2.	Deselect all data types except for "YouTube and YouTube Music".
3.	Proceed to export your data.
4.	Download the archive and extract it to a folder on your pc.

Setting Up the Project
1. Organizing Files
•	Create a new folder on your computer for this project.
•	Place all four Python scripts (youtube.py, youtwo.py, my_functions.py, and final_script.py) in this folder.
•	Move the Google Takeout data folder into the project directory.

2. Setting Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.
1.	Install venv if you don't have it: pip install venv
2.	Create a virtual environment: python - m venv name_of_environment
3.	To activate the virtual environment: name_of_environment\Scripts\activate


3. Installing Dependencies
Ensure that your virtual environment is active, then install the required libraries:
1.	Install the Google API client: pip install google-api-python-client in the youtube.py
2.	Install Pandas for data manipulation: pip install pandas install  in final final_script.py

Script Descriptions and Execution
1. youtube.py
Purpose: This script retrieves video details from your "Watch Later" playlist using the YouTube API.
Setup:
•	Enter your API key in the api_key variable within the script.
•	Specify the file path of the CSV file containing video IDs in the Watch_later_csv_file variable.
Execution:
•	Run the script to fetch video details. The output will be a list of dictionaries containing details for each video in your playlist.
•	You can verify the success by printing video_details.
Troubleshooting:
•	If you encounter issues with the API call, ensure that your API key is correct and that the required modules are installed.
2. youtwo.py
Purpose: This script stores the data retrieved from the API into a CSV file for further analysis.
Setup:
•	Create a CSV file within your project folder where the video data will be stored.
•	Update the video_data variable with the file path of the CSV file.
Execution:
•	Run the script to store the video data in the CSV file.
•	Check the CSV file to ensure it has been populated with the correct data.

3. my_functions.py
Purpose: This script contains utility functions that are used by the other scripts. It may include functions for data processing, filtering, and more.
Note:
•	You don’t need to run this script directly; it will be used by youtube.py, youtwo.py, and final_script.py as needed.


4. final_script.py
Purpose: This is the final script that curates the list of 10 YouTube video links based on your preferred duration.
Execution:
•	Run the script after youtube.py and youtwo.py have successfully completed.
•	The script will filter the videos based on the duration you specify and output a list of 10 video links.
Output:
•	The script will display the final list of curated video links, which you can then use as desired.
Final Notes
Thank you for using this project! If you encounter any issues or have questions, feel free to reach out.



