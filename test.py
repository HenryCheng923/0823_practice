import requests
r = requests.get('https://www.cnyes.com', headers = header, verify=False)
r.encoding()
print(r.rest)