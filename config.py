import os

import psutil


class Config:
    APP_ID = int(os.environ.get("29490954"))
    API_HASH = os.environ.get("dbd8f5af56b0f6e16327c20a84eece99")
    BASE_LANGUAGE = os.environ.get("BASE_LANGUAGE", default="en")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    BOT_OWNER = int(os.environ.get("7660860610"))
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    IS_HEROKU = os.environ.get("DYNO", default="").startswith("worker.")
    LOCKFILE = "/tmp/unzipbot.lock"
    LOGS_CHANNEL = (
        int(os.environ.get("-1002319037245"))
        if os.environ.get("-1002319037245").strip("-").isdigit()
        else os.environ.get("-1002319037245")
    )
    MAX_CONCURRENT_TASKS = 75
    MAX_MESSAGE_LENGTH = 4096
    MAX_CPU_CORES_COUNT = psutil.cpu_count(logical=False)
    MAX_CPU_USAGE = 80
    # 512 MB by default for Heroku, unlimited otherwise
    MAX_RAM_AMOUNT_KB = 1024 * 512 if IS_HEROKU else -1
    MAX_RAM_USAGE = 80
    MAX_TASK_DURATION_EXTRACT = 120 * 60  # 2 hours (in seconds)
    MAX_TASK_DURATION_MERGE = 240 * 60  # 4 hours (in seconds)
    # Files under that size will not display a progress bar while uploading
    MIN_SIZE_PROGRESS = 1024 * 1024 * 50  # 50 MB
    MONGODB_URL = os.environ.get("mongodb+srv://fibegi:8oV4fjNNVasSfcoY@cluster0.jp8thup.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    MONGODB_DBNAME = os.environ.get("MONGODB_DBNAME", default="Unzipper_Bot")
    TG_MAX_SIZE = 2097152000
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    VERSION = os.environ.get("UNZIPBOT_VERSION", default="7.3.0")
