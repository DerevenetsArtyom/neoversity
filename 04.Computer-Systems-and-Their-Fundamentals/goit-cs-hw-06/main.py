import asyncio
from multiprocessing import Process

from handlers import run_http_server, run_socket_server


if __name__ == "__main__":
    # Run HTTP server
    http_server_process = Process(target=run_http_server)
    http_server_process.start()

    # Run sockets server
    asyncio.run(run_socket_server())

    http_server_process.join()
