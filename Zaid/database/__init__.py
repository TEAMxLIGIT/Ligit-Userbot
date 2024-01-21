import motor.motor_asyncio
from config import MONGO_URL  # Make sure MONGO_URL is imported from your config

cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
dbb = cli.program
