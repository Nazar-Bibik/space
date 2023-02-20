import sys


class Request:
    def __init__():
        pass

    def find_delimiter(binary: bytes) -> str:
        for octane in binary:
            if octane == "\r":
                try:
                    if binary[octane.index + 1] == "\n":
                        return "\\r\\n"
                    else:
                        return "\r"
                except Exception as err:
                    print(err)
                    sys.exit(err.errnum)