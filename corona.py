import urllib.request, json

url = "https://api.covid19api.com/live/country/austria/status/confirmed"

r = urllib.request.urlopen(url)

data = json.loads(r.read().decode())

last = len(data) - 1

confirmed = "Confirmed"
deaths = "Deaths"
recovered = "Recovered"

print(f"Heute insgesamt {str(data[last][confirmed])[0:3]}.{str(data[last][confirmed])[3:6]} Covid-19 Fälle; {str(data[last][recovered])[0:3]}.{str(data[last][recovered])[3:6]} Genesene und {str(data[last][deaths])[0:2]}.{str(data[last][deaths])[2:5]} Tode. (Tag {last} seit Beginn der Zählung)")