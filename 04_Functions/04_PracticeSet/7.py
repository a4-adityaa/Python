#use request module

import requests

link = requests.get("https://api.github.com" )
print(link.text)