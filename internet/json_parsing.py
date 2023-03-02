# Parse JSON data of USGS significant earthquakes in the past month

import urllib.request
import json

# Make HTTP request
url = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson")
if (url.getcode() == 200):
    data = url.read()
else:
    print("HTTP error: " + str(url.getcode()))

# Parse JSON data
json_data = json.loads(data)

print(json_data["metadata"]["title"]) # USGS Significant Earthquakes, Past Month
count = json_data["metadata"]["count"]
print(str(count) + " events recorded") # x events recorded
print("----------------------------")

print("All earthquakes:")
for i in json_data["features"]:
    print(i["properties"]["place"]) # Location of earthquake
print("----------------------------")

print("Earthquakes of magnitude 4.0 or greater:")
for i in json_data["features"]:
    if i["properties"]["mag"] >= 4.0:
        print(i["properties"]["mag"], i["properties"]["place"])
print("----------------------------")

print("Earthquakes that were felt:")
for i in json_data["features"]:
    felt_reports = i["properties"]["felt"]
    if (felt_reports != None):
        if felt_reports > 0:
            print(i["properties"]["place"] + " reported " + str(felt_reports) + " times")