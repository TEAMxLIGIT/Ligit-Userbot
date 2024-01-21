import motor.motor_asyncio
import pymongo

from config import MONGO_URL

cli = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
dbb = cli.program
