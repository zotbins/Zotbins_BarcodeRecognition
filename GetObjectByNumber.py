import requests
import json

#number must be a string
def getObjectByNumber(number):
    url = "https://api.barcodespider.com/v1/lookup"

    querystring = {"upc":number}

    headers = {
        'token': "74d14d4b07e53d3e66a8",
        'Host': "api.barcodespider.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    x = json.loads(response.text)

    itemName = x["item_attributes"]['title']

    #print(itemName)
    return (itemName)

#test
#myNum = '49000052350'
#print(getObjectByNumber(myNum))
