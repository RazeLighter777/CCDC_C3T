import socket
import threading
import time
bind_ip = "0.0.0.0"
bind_port = 23
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip, bind_port))
# This is the thread we handle the data from  the client
def handle_client(client_socket):
    # emulate a terminal
    # send a shell prompt
    while True:
        client_socket.send(b"bash$ ")
        # read until the client sends a newline
        buff = b""
        while True:
            buff += client_socket.recv(1)
            if buff.endswith(b"\n") or buff.endswith(b"\r") or not buff:
                break
        # write their request, timestamp, and IP to a file
        # if request just isn't empty or whitespace
        if buff and buff.strip():
            with open("/var/log/telpot.log", "a") as f:
                timestr = time.strftime("%Y-%m-%d %H:%M:%S")
                ipstr = client_socket.getpeername()[0]
                f.write(timestr + " " + ipstr + " " + buff.decode("utf-8"))
        #flush the buffer
        client_socket.send(buff)
while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    # activate the function to handle the data from client
    client_handler = threading.Thread(target = handle_client, args=(client,))
    client_handler.start()

