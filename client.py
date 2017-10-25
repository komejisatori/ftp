import socket
import time
import threading
size = 8192
def client_listening(sock):
    while True:
        if sock.recv(size) != 0:
            print(sock.recv(size))

try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
  print("cannot reach the server")
print(sock.recv(size))
#msg_list = message_sequence()
t = threading.Thread(target=client_listening,args=(sock,))
t.start()
for i in range(50):
    msg = str(i).encode(encoding="utf-8")
    sock.sendto(msg, ('localhost', 9876))
sock.close()