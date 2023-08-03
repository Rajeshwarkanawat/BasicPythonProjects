import requests
import json
import win32com.client as wincom

speak= wincom.Dispatch("SAPI.Spvoice")
city=input("Enter the name of the city\n")
url=f"WeatherAPI+KEY{city}"
r= requests.get(url)

print(r.text)
wdic = json.loads(r.text)
print(wdic["current"])
speak.Speak(r.text)