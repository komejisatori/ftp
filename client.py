import socket
size = 8192

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print("cannot reach the server")
for i in range(50):
    msg = str(i).encode(encoding="utf-8")
    sock.sendto(msg, ('198.199.119.37', 9876))
while True:
    print(sock.recv(size))
sock.close()