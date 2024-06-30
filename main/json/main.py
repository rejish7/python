# import json
# data={}


# json_strings=json.dumps(data)
# python_duct=json.loads(data)


import requests
url="https://jsonplaceholder.typicode.com/photos"

response = requests.get(url)
# print(response)
data  = response.json()
for i in data:
    #  print(i['title'])
     print(i['thumbnailUrl'])
     print('=================')
