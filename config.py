import os

API_ID = API_ID = 20589899

API_HASH = os.environ.get("API_HASH", "62d81c8040fffee65705d0df9931a07b)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7162386874:AAFfjkS7K2WOpIse1Fl78mF3dHRuYp541fo")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5971411129))

LOG = -1002042415574

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6804641253").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


