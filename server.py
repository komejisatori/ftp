import socket

size = 8192

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9876))

msg_count = 0
try:
  while True:
    data, address = sock.recvfrom(size)
    msg_sendback = str(msg_count).encode(encoding="utf-8")
    msg_sendback += data.upper()
    msg_count += 1
    #print(msg_sendbacklist)
    sock.sendto(msg_sendback, address)
finally:
  sock.close()