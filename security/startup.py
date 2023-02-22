# Copyright (C) 2023  Nazar Bibik

import os


USER_INPUT_AGREE = ["YES", "Yes", "yes", "y", "Y"]
USER_INPUT_DECLINE = ["NO", "No", "no", "n", "N"]

    

def set_environment_variables(file_path=""):
    """ Read and save env variables from file. """
    try:
        for name, value in \
            open_env_file(file_path if file_path != "" else ".env"):
            try:
                os.environ[name] = value
            except Exception as err: 
                err.add_note("Failed to set env variable " + name + ".")
                raise err
    except FileNotFoundError as err:
        if file_path!="":
            print(" Invalid path to: environment variables file. ")
            print(" Attempting opening default .env file ")
            set_environment_variables()
        else:
            err.add_note(" Default environment file abscent. ")
            err.add_note(" Make sure there is an .env file in root directory, \
                or provide a path to an .env file. ")
            raise
    except:
        raise
        

# generator for env file
def open_env_file(file_path=""):
    with open(file_path, "r") as file:
        for line in file:
            if not line:
                continue
            if line.startswith("#"):
                continue
            yield line.split("=", 1)