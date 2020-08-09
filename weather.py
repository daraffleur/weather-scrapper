import requests
from bs4 import BeautifulSoup
import csv
page = requests.get("https://www.bbc.com/weather/1275339")
soup = BeautifulSoup(page.content, 'html.parser')
fortheen_day = soup.find(id="wr-forecast")
loc=soup.find(class_="wr-c-location")
print(loc)
doc=fortheen_day.find_all(class_='wr-js-day')
tonight=doc[0]
print(tonight.prettify())
location=loc.find(id="wr-location-name-id").get_text()
period=tonight.find(class_="wr-day__title").get_text()
temp = tonight.find(class_="wr-day__temperature").get_text()
short_desc = tonight.find(class_="wr-day__details__weather-type-description").get_text()

print(location)
print(period)
print(temp)
print(short_desc)


# Open writer with name
file_name = "weather.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

# write a new row as a header
f.writerow(['Day', 'Description', 'Temperature'])

period_tags = fortheen_day.select(".wr-day__title")
periods = [pt.get_text() for pt in period_tags]
temps = [t.get_text() for t in fortheen_day.select(".wr-day__temperature")]
short_descs = [sd.get_text() for sd in fortheen_day.select(".wr-day__details__weather-type-description")]

print('periods', periods)
print('temps',temps)
print('short_descs', short_descs)

print('Writing rows')
    # add the information as a row into the csv table
f.writerow([periods, short_descs, temps])