import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

#you need a specific api key to make this code work. you can get your api key from Google Cloud Console.
api = "AI******"
address = "https://maps.googleapis.com/maps/api/geocode/json?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    user_address = input("Enter an address: ")
    url = address + \
        urllib.parse.urlencode({"address": user_address, "key": api})

    url_search = urllib.request.urlopen(url, context=ctx)
    data = url_search.read().decode()
    print(url)
    print("characters: ", len(data))

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("===== Sorry, failed to retrieve =====")
        continue

    print(json.dumps(js, indent=4))
    # for loc in js["results"]["formatted_address"]:
    #     print("Latitude: ", ["location"]["lat"])
    #     print("Longitude: ", ["location"]["lng"])
    print(js["results"][0]["place_id"])
