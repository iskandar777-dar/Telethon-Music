import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5661784900:AAHRsreMNSArNM2uU-auqG4pWTWY9LYQdp4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQAhIHQAHtV8EKmrZKJrTs0q0tCnn7RQzjJYBhJRpmc-5Vg65PJP7mRLecdTxvQgbCdOlC7x7EI2DAPCgrG9BdZhA5tEqB5sXi-du2KPLY6rG_Y7rl97PEr4TFwmJ2Q8d6hFgi1UFB-wzfDnKLPhRyNGg1OooVhOl366qmo-6ufPMdeUR_sibD9vGi4N_3ysLrDoSYYduvTV8dAF4-K4ezq1y8wO7iX84mfVRCS2BdVNYXdbXdYx0umDJ5lCi4xwgm0tU8f8aNQ7hwBguc-j-KJAOWg-7Vx4epYW44vtg5_bmbyk-bTYmA25e7P2MypjW_ditUG4QkXsSnHL3DpX6M-a9imVugAAAABqRVX4AA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "darmimusikbot")
    SUPPORT = os.environ.get("SUPPORT", "medsupportt") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "medchannell") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1782928888")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
