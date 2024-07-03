import requests

url = 'https://ludwpfeiffer.sharepoint.com/sites/PfeifferDhaka'
r = requests.post(url, json={'Item Serial No' : "1", 'Name of work including materials' : "Work of a bulldozer on the dump", 'Units' : "m3", 'Quantity': "1940", 'Date' : "2020-01-26", 'Work Done': "No"})
print(r.json())
