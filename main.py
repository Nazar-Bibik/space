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
import security.startup
from security.manager import Manager
from server import Request
from server import ServerMap
import server

        
def _create_socket() -> socket.socket:
    try:
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    except socket.error as err:
        print("Unexpected ERROR during creation of socket object.")
        print(err.strerror)
        sys.exit(err.errno)
    _bind_socket(new_socket)
    return new_socket


def _bind_socket(new_socket: socket.socket):
    host_address = os.environ["SPACE_IP"]
    host_port = int(os.environ["SPACE_PORT"])

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
    print("The following port number was binded to socket: " + str(host_port))


def main() -> int:

    security.startup.set_environment_variables()

    servermap = ServerMap()

    with _create_socket() as server_socket:

        # Open the Server to network
        server_socket.listen(5)

        # Make a user input thread
        inputThread = security.startup.InputThread(server_socket)
        inputThread.start()

        # Accept connection, recieve data and server response in a loop until user input
        while inputThread.keep_alive():
            
            connection, addr = server_socket.accept()
            # connection.settimeout(2)
            with connection:
                manager = Manager(addr)

                # HTTP processing
                while manager.keep_alive():
                    #create request object
                    request = Request()
                    try:
                        while manager.uncomplete_request(request):
                            data = connection.recv(manager.buffer_size())
                            if not data:
                                break
                            request.add_data(data)                        
                        request.assemble()
                        manager.verify_request(request)
                    except Exception as err:
                        manager.catch(err)
                        print(err)
                        manager.flush(connection, data)
                        
                    # Form response and send
                    response = server.serve(request, servermap, manager.exception())

                    print(connection.send(response))
                    # manager.kill()

                connection.close()

        server_socket.close()

    print("Successful execution")
    return 0


if __name__ == "__main__":
    sys.exit(main())