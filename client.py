import socket
import os
import sys


def _create_socket() -> socket.socket:
    try:
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #since this is a `practice project`, no need for multithreaded server 
        new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    except socket.error as err:
        print("Unexpected ERROR during creation of socket object.")
        print(err.strerror)
        sys.exit(err.errno)
    _bind_socket(new_socket)
    return new_socket


def _bind_socket(new_socket: socket.socket):
    host_address = os.environ["SPACE_IP"]
    host_port = 9056

    while True:
        try:
            new_socket.bind((host_address, host_port))
            break
        except OSError as err:
            if err.errno == 10048:
                if host_port >= 65535:
                    print("Could not bind any port to the socket")
                    print("List of possible port numbers exhausted. MAX=65536")
                    new_socket.close()
                    sys.exit(err.errno)
                host_port += 1
            else:
                print(err)
                sys.exit(err.errno)

    if host_port != int(os.environ["SPACE_PORT"]):
        print("Could not bind socket to .env defined port number: " + str(os.environ["SPACE_PORT"]))
        os.environ["SPACE_PORT"] = str(host_port)
    print("Client listens with socket: " + str(host_port))


def main() -> int:

    with _create_socket() as listen_socket:
        while True:
            uinput = input("Type anything ")
            if uinput == "exit":
                listen_socket.shutdown()
                break
            listen_socket.connect(("192.168.8.125", 8000))
            while True:
                listen_socket.sendall(bytes("GET file/test.txt HTTP/1.1\r\nUser-Agent: myself\r\nAccept: */*\r\nHost: 192.168.8.125:8000\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate, br\r\n\r\n'", "utf-8"))
                data = listen_socket.recv(2048)
                print(str(data))

    return 0

if __name__ == "__main__":
    sys.exit(main())