from queue import Queue
import time

# Create a queue of requests
requests_queue = Queue()


def generate_request(request_id):
    new_request = f"Request {request_id}"
    requests_queue.put(new_request)
    print(f"Request added: {new_request}")


def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"Processing {request}...")
        time.sleep(2)  # Simulating request processing time
        print(f"{request} processed")
    else:
        print("Queue is empty")


def main():
    request_id = 1

    try:
        user_input = input("Enter 'q' to quit or 'Enter' to continue: ")
        while True:
            if user_input == "q":
                break
            generate_request(request_id)
            process_request()
            request_id += 1
            time.sleep(2)  # Simulating time between generating new requests
    except KeyboardInterrupt:
        print("Program terminated by user.")


if __name__ == "__main__":
    main()
