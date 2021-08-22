#####################
# Imports           #
#####################

import requests

#####################
# Globals           #
#####################

BASE = "http://127.0.0.1:5000/"

#####################
# Main              #
#####################

data = [ 
        { "id": 1, "likes": 78, "name": "Joe", "views": 100000 },
        { "id": 2, "likes": 36, "name": "Rob", "views": 900000},
        { "id": 3, "likes": 27, "name": "Tim", "views": 400000}
]

for i in range(len(data)):
    
    index = str(i)

    view = "video/" + index

    response = requests.put(BASE + view, data[i])

    print(response.json())

response = requests.get(BASE + "video/2")

print(response.json())
