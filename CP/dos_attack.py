import requests
import threading

target_url = "http://127.0.0.1:5000"
total_requests = 12000

def send_request():
    try:
        requests.get(target_url)
    except:
        pass

print("🚀 Starting HTTP flood simulation...\n")

for i in range(total_requests):
    threading.Thread(target=send_request).start()

print("Simulation launched.")