import os
import asyncio
import logging
import json
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

import websockets

logging.basicConfig(level=logging.INFO)


SOCKET_SERVER_HOST = os.getenv("SOCKET_HOST")
SOCKET_SERVER_PORT = int(os.getenv("SOCKET_PORT"))


class SocketHandler:
    """Class that handles all requests to Socket server"""

    async def provide_db_collection(self):
        """Function that provides asynchronous connection to Mongo DB"""

        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        domain = os.getenv("DB_DOMAIN")
        port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        collection = os.getenv("DB_COLLECTION")

        client = AsyncIOMotorClient(f"mongodb://{username}:{password}@{domain}:{port}/")
        return client.get_database(db_name).get_collection(collection)

    async def message_handler(self, message: str):
        """Asynchronous function that handles interactions with database"""
        db_collection = await self.provide_db_collection()

        message_dict = json.loads(message)
        message_dict["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        result = await db_collection.insert_one(message_dict)
        logging.info("Message is inserted to DB with ID: %s", result)

    async def websocket_handler(self, websocket):
        """Asynchronous function that handles messages on websockets"""
        message = await websocket.recv()
        await self.message_handler(message)


async def run_socket_server(handler_class=SocketHandler):
    """Asynchronous function that runs Socket server that interacts with database"""
    server_address = (SOCKET_SERVER_HOST, SOCKET_SERVER_PORT)
    socket_server = handler_class()

    try:
        async with websockets.serve(socket_server.websocket_handler, *server_address):
            logging.info("Socket server is listening on port %s", SOCKET_SERVER_PORT)
            await asyncio.Future()
    except (KeyboardInterrupt, asyncio.exceptions.CancelledError):
        logging.info("Socket server is interrupted")
