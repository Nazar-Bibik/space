# Copyright (C) 2023  Nazar Bibik

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import sys
import os
import socket
import errno
import secutiry.startup

        
def create_socket() -> socket.socket:
    #since this is a `student project`, no need for multithreaded server 
    try:
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, False)
    except:
        print("Unexpected ERROR during creation of socket object.")
        sys.exit(1)
    bind_socket(new_socket)
    return new_socket


def bind_socket(new_socket: socket.socket):
    host_address = os.environ["SPACE_IP"]
    host_port = int(os.environ["SPACE_PORT"])
    
    while True:
        if host_port >= 65536:
            print("Could not bind any port to the socket")
            print("List of possible port numbers exhausted. MAX=65536")
            new_socket.close()
            sys.exit(1)
        try:
            new_socket.bind((host_address, host_port))
            break
        except:
            host_port += 1

    if host_port != int(os.environ["SPACE_PORT"]):
        print("Could not bind socket to .env defined port number: " + str(os.environ["SPACE_PORT"]))
        os.environ["SPACE_PORT"] = str(host_port)
    print("The following port number was binded to socket: " + str(host_port))



def main() -> int:

    secutiry.startup.set_environment_values()

    with create_socket() as server_socket:
        server_socket.listen(0)
        conn, addr = server_socket.accept()
        data = conn.recv(4096)
        if data:
            print(data)
        conn.send(data)
        conn.close()
        server_socket.close()


    print("Succsessful execution (hopefully)")
    return 0

if __name__ == "__main__":
    sys.exit(main())