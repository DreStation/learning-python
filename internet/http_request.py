import urllib.request

# Make a simple HTTP request
url = urllib.request.urlopen("https://drestation.com")
print("HTTP response code: " + str(url.getcode()))

# Scrape all the HTML from the page
data = url.read()
print(data)