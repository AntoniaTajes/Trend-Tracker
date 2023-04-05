# Trend Tracker
This is a simple Python program that uses the Google Trends API to track the popularity of a particular search term over time. This program can be used to track the popularity of any trend over time, which can provide some insight into whether it's gaining or losing momentum.

Getting Started
To use this program, you'll need to have a Google account and a Google Trends API key. You can sign up for an API key at https://developers.google.com/trends/api/guides/getting-started.

Once you have your API key, open main.py in a text editor and replace the API_KEY variable with your key. Save the file and then run it using Python.

css
Copy code
python main.py
The program will make a request to the Google Trends API and then plot the results on a graph. The default search term is "trend" in the United States over the past 12 months, but you can modify the program to track other search terms or in other locations by changing the comparisonItem parameter in the API request.

Dependencies
This program requires the following dependencies:

requests
matplotlib
You can install these dependencies using pip:

Copy code
pip install requests matplotlib
License
This program is licensed under the MIT License. See the LICENSE file for details.
