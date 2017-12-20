import time
import json
import requests


#  Replace the "api_key" variable with your own OpenWeather.org API Key


def api_call_5day(zipcode):
    base_url = "http://api.openweathermap.org/data/2.5/"
    type_5day_zip = "forecast?zip="
    units_imp = "&units=imperial"
    api_key = "&appid=<<YOUR OPENWEATHER.ORG API KEY>>"
    api_call = requests.get(base_url + type_5day_zip + zipcode + units_imp + api_key)
    decoded = json.loads(api_call.text)
    return decoded

def api_call_today(zipcode):
    base_url = "http://api.openweathermap.org/data/2.5/"
    type_today_zip = "weather?zip="
    units_imp = "&units=imperial"
    api_key = "<<YOUR OPENWEATHER.ORG API KEY>>"
    api_call = requests.get(base_url + type_today_zip + zipcode + units_imp + api_key)
    decoded = json.loads(api_call.text)
    return decoded

zip_input = raw_input("Please enter the 5 digit zip code:  ")

api_5day = api_call_5day(zip_input)['list']

api_today = api_call_today(zip_input)['main']

list_temp = []

for i in range(len(api_5day)):
    api_day = time.strftime('%A', (time.localtime(api_5day[i]['dt'])))
    today = time.strftime('%A', time.localtime())
    temp = api_5day[i]['main']['temp']
    if today == api_day:
        list.append(list_temp, int(round(temp)))


print("Here is the weather for today - {}".format(time.strftime('%a, %b %d, %Y', time.localtime())))
print("")
print("    The current temp is {} degrees".format(int(round(api_today['temp']))))
print("    The high for today is expected to be {} degrees".format(max(list_temp)))
print("    The low for today is expected to be {} degrees".format(min(list_temp)))
