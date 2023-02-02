import pinterest
import os
from dotenv import load_dotenv
from tools import getFullPath

BASE_DIR = getFullPath()
load_dotenv(f"{BASE_DIR}/day95/secrets.env") # URL (not secret)
load_dotenv(f"{BASE_DIR}/day95/secrets.local.env") # KEY (secret)
REDIRECT_URI = os.getenv("REDIRECT_URI")
APP_ID = os.getenv("APP_ID")
TOKEN = os.getenv("TOKEN")

# Generate OAuth2 authorization link
link = pinterest.oauth2.authorization_url(APP_ID, REDIRECT_URI)
print(link)

# Initialize API by passing OAuth2 token
api = pinterest.Pinterest(token=TOKEN)
print(api)

print(api.me())