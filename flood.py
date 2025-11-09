import socket
import threading

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", 5173))
            s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            s.close()
        except:
            pass

for i in range(200):  
    threading.Thread(target=flood).start()