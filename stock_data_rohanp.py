import requests
import urllib.request
import time

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval":"1min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

headers = {
	"X-RapidAPI-Key": "d43cfa73fdmsh803324fa1ae12bap12efbajsn7f40bf0e4113",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json()
last_refereshed = data["Meta Data"]["3. Last Refreshed"]
price = data["Time Series (1min)"][last_refereshed]["2. high"]

while True:
    with urllib.request.urlopen("https://api.thingspeak.com/update?api_key=HIRJLI9FJ809OD4L&field1=0"+str(price)) as url:
        s = url.read()
        print("Sent new data!")
    time.sleep(60)