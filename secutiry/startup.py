# Copyright (C) 2023  Nazar Bibik

import os
import sys
import errno


USER_INPUT_AGREE = ["YES", "Yes", "yes", "y", "Y"]
USER_INPUT_DECLINE = ["NO", "No", "no", "n", "N"]

    

def set_environment_variables(file_path=""):
    "read env variables from file and save into environment"
    try:
        for name, value in \
            open_env_file(file_path if file_path != "" else ".env"):
            try:
                os.environ[name] = value
            except Exception as e: 
                print("Failed to set env variable " + name + ".")
                print(Exception())
    except errno.ENOENT:
        if file_path!="":
            print("Invalid path to: environment variables file.")
            print("Attempting opening default .env file")
            set_environment_variables()
        else:
            print("Default environment file abscent.")
            print("Make sure there is an .env file in root directory, or provide a path to an .env file.")
            sys.exit(1)


def open_env_file(file_path=""):
    "generator for env file"
    with open(file_path, "r") as file:
        for line in file:
            if not line:
                continue
            if line.startswith("#"):
                continue
            yield line.split("=", 1)