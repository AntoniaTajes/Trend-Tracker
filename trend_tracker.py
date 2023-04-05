import requests
import json
import matplotlib.pyplot as plt

# API request
url = 'https://trends.google.com/trends/api/widgetdata/multiline'
params = {
    'hl': 'en-US',
    'tz': '-120',
    'req': json.dumps({
        "time":"today 12-m",
        "resolution":"WEEK",
        "locale":"en-US",
        "comparisonItem":[{"geo":{"country":"US"},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":"fashion trend"}]}}]
    })
}
headers = {
    'content-type': 'application/json'
}

# This will make the API request and parse the response
response = requests.get(url, params=params, headers=headers)
json_data = json.loads(response.text.replace(")]}',", ""))

# this will extract the data and plot it
timeline_data = json_data['default']['timelineData']
data = [int(point['value'][0]) for point in timeline_data]
dates = [point['formattedTime'] for point in timeline_data]
plt.plot(dates, data)
plt.title('Popularity of "fashion trend" search term over time')
plt.xlabel('Date')
plt.ylabel('Search interest')
plt.show()
