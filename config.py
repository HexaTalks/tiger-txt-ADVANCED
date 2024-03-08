import os

API_ID = API_ID = 29509604

API_HASH = os.environ.get("API_HASH", "7543d780627ea4a25da5fe5696167440)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6984025218:AAG00eo_USPsOEuUfExdgwPFChrksaQG5FQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5971411129))

LOG = -1002039122754

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6804641253").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


