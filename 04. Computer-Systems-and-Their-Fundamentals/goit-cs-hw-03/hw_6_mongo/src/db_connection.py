"""Module that provides connection with MongoDB"""

from pymongo import MongoClient

config = {
    "dbname": "cats",
    "user": "user",
    "password": "password12345",
    "host": "localhost",
    "port": "27017",
    "collect": "my_collection",
}

username = config.get("user", "user")
password = config.get("password", "pass")
domain = config.get("domain", "domain")
db_name = config.get("dbname", "cats")
port = config.get("port", "27017")
collect = config.get("collect", "my_collection")

client = MongoClient(f"mongodb://{username}:{password}@{domain}:{port}/")
db = client[db_name]
collection = db[collect]
