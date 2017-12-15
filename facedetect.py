#0e00a2f93e7f45d699edff44e79c68e1

import cognitive_face as CF
import requests
import httplib
import urllib
import json
from pprint import pprint
from os.path import expanduser
from io import BytesIO
from PIL import Image, ImageDraw

KEY = '03d0c97c81924a9196d41e066a4c4b2b'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '03d0c97c81924a9196d41e066a4c4b2b'
}

params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses',
})

url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect?%s' % params
img = open(expanduser('3.png'), 'rb')
response = requests.post(url, data=img, headers=headers)
data = response.json()
print ("Response:")
print (json.dumps(data, sort_keys=True, indent=2))
if response.status_code != 200:
    raise ValueError(
        'Request to Azure returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
)

#Display the image in the users default image browser.
img = Image.open('3.png')
img.show()