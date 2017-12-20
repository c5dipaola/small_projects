import time
import json
import requests


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def api_call_5day(zipcode):
    base_url = "http://api.openweathermap.org/data/2.5/"
    type_5day_zip = "forecast?zip="
    units_imp = "&units=imperial"
    api_key = "&appid=<<YOUR OPENWEATHER.ORG API KEY>>"
    api_call = requests.get(base_url + type_5day_zip + zipcode + units_imp + api_key)
    decoded = json.loads(api_call.text)
    return decoded


zip_input = raw_input("Please enter the 5 digit zip code:  ")

city = api_call_5day(zip_input)['city']['name']

print("#" * 75)
print("")
print("You've entered the zip code {}.".format(zip_input))
print("Here is your 5 day forecast for the city of {}.".format(city))
print("")
print("#" * 75)

dint = 0
x = 0
counts = len(api_call_5day(zip_input)['list']) - 1
while dint <= counts:
    day = time.strftime('%w', (time.localtime(api_call_5day(zip_input)['list'][dint]['dt'])))
    date = time.strftime('%A, %B %d, %Y', (time.localtime(api_call_5day(zip_input)['list'][dint]['dt'])))
    now_temp = api_call_5day(zip_input)['list'][dint]['main']['temp']
    conditions = api_call_5day(zip_input)['list'][dint]['weather'][0]['description']
    time_now = time.strftime('%H:%M', (time.localtime(api_call_5day(zip_input)['list'][dint]['dt'])))
    for delta in day:
        int_day = int(day) + 1
        if delta == day:
            if x != int_day:
                print("")
                raw_input("Press enter to continue...")
                print("")
                print("=" * 75)
                print("")
                print("======  The weather for {} will be  ======".format(date))
                print("")
                print(" " * 4 + "The weather at {} will be:".format(time_now))
                print(" " * 8 + "Expected Temperature is {}".format(now_temp))
                print(" " * 8 + "Expect {}".format(conditions))
                print("")
                dint += 1
                x = int(day) + 1
            else:
                print(" " * 4 + "The weather at {} will be:".format(time_now))
                print(" " * 8 + "Expected Temperature is {}".format(now_temp))
                print(" " * 8 + "Expect {}".format(conditions))
                print("")
                dint += 1
