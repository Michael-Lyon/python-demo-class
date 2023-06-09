import urllib.request
import urllib.parse
import urllib.error
import json
import ssl


api_key = False
# if you have a Google API key, enter it here
# api_key = 'AIZasy__IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


if api_key is False:
    api_key = 42
    serviceurl = 'https://py4e-data.dr-chuck.net/json?'

else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


# ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    params = dict()
    params['address'] = address
    if api_key is not False:
        params['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrived', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dump(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
