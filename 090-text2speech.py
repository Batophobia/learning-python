import requests
import os
from dotenv import load_dotenv
from tools import getFullPath

BASE_DIR = getFullPath()
load_dotenv(f"{BASE_DIR}/day87/secrets.env") # URL (not secret)
load_dotenv(f"{BASE_DIR}/day87/secrets.local.env") # KEY (secret)
KEY = os.getenv("KEY")
URL = os.getenv("URL")
# Daily Requests: 350 (Free Tier) [100KB per request]

user = input("Enter test to speechify\n")

### hl / v Options ###
# Australia:
#   "en-au:Zoe"
#   "en-au:Isla"
#   "en-au:Evie"
#   "en-au:Jack"
# Canada:
#   "en-ca:Rose"
#   "en-ca:Clara"
#   "en-ca:Emma"
#   "en-ca:Mason"
# Great Britain:
#   "en-gb:Alice"
#   "en-gb:Nancy"
#   "en-gb:Lily"
#   "en-gb:Harry"
# India:
#   "en-in:Eka"
#   "en-in:Jai"
#   "en-in:Ajit"
# Ireland:
#   "en-ie:Oran"
# United States:
#   "en-us:Linda"
#   "en-us:Amy"
#   "en-us:Mary"
#   "en-us:John"
#   "en-us:Mike"

params = {
  "key": KEY,
  "hl": "en-ca",
  "v": "Clara",
  "c": "MP3",
  "f": "16khz_16bit_stereo",
  "src": user
}
resp = requests.get(URL, params=params)

with open('./day87/output.mp3', 'wb') as f:
    f.write(resp.content)