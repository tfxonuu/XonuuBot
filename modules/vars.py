#shahnawaz
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27293287"))
API_HASH = environ.get("API_HASH", ""052041b03a7028b3bd11da3143cffa0e)
BOT_TOKEN = environ.get("BOT_TOKEN", "8033732232:AAF_W5lgzZhFjTEZJ0qnMTxtnFqqUZTBuEo")

OWNER = int(environ.get("OWNER", "7533484450"))
CREDIT = environ.get("CREDIT", "𝕾𝖍𝖆𝖍𝖓𝖆𝖜𝖆𝖟")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7533484450').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7533484450').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

