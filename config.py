from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 18329555)  # api id
API_HASH = environ.get("API_HASH", "7bf83fddf8244fddfb270701e31470a8")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7289601896:AAG0A32TgmJ-vyngI0UUz7dJdewc9pcFpps")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-17047.c17.us-east-1-4.ec2.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 17047)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "XCZ3u8NzVm7F2lK1ZmhbBqWs0tspN5em"
)  # redis password


ADMINS = [1195233863]
OWNER_ID = 1195233863  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1001582920811  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1001582920811
DUMP_CHANNEL = -1001582920811


# Config
COOKIE = environ.get("COOKIE", "csrfToken=SpHNTDY8Y6yRXSxBbMXDJuzC; __bid_n=190389845dfd0e2b634207; _ga=GA1.1.814234588.1718936423; g_state={"i_l":0}; ndus=YSZ_IK4teHuif6iSBth9G4p6ZtQ7UyQnCjQiXEaN; ndut_fmt=1D7155880C66AF834693B31423D00C85E1C6DF72F777B053FF06F42AE443AC3E; perf_dv6Tr4n=1; ab_sr=1.0.1_MzczMzBlYmI1NGY5Zjg3ZGIwNzlmMzRmYzI2MjU1OGNjMDYxZmZkZTRlYWE0OWRlMGNiNjAwYzkwOWFjODA3OTdjOTM1MzQ2OTA1YTU5ZDVjMjdjOGNkYzczMzc0OGRlNDU4MDNiM2Q3N2I4M2ZlNTM0ZTFjMmFhZDFlMzQ3NWY3YmFlYjAyYjA3ODI1YjNlNWIwMWFlZTJiYzc3ZDVkMg==; ab_ymg_result={"data":"7e0c9ae60093d5a88f4b4a6a92197e20518e361f5e5ead0c6beae1136d23f0201d075deb9f47af2cfd09497b6b96137731f916c9c27732bae37b4cc7ce6eaf1067355a97e59605c75ef2cb541dca7535f4a0a6f64f42fa0f81c1202f0d8e1042eac8bf038d497fa074bcb979725f464b7589d63c8aedf21244cb913789fc9f23","key_id":"66","sign":"764d79e0"}; _ga_06ZNKL8C2E=GS1.1.1718936422.1.1.1718936535.25.0.0")
