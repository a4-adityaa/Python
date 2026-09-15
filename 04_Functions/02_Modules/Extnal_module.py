# Extermal Modules installed using pip-install
import requests

r= requests.get("https://www.google.com")
print(r.text)