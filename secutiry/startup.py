# Copyright (C) 2023  Nazar Bibik

import os
import sys

USER_INPUT_AGREE = ["YES", "Yes", "yes", "y", "Y"]
USER_INPUT_DECLINE = ["NO", "No", "no", "n", "N"]

def main():
    print(">STARTUP:")
    while True :
        print("Do you want to use default startup options? (Y/n)")
        _console_input = input()
        if _console_input in USER_INPUT_AGREE & _console_input in USER_INPUT_DECLINE:
            break
        else:
            print("Incorrect input. Please, use 'y' or 'n' for this request.")
    #CONTINUE FROM HERE
    set_environment_values("")
    

def set_environment_values(file_path=""):
    save_environment_values(import_environment_values(file_path))


def save_environment_values(environment_variables_input: str):
    if len(environment_variables_input) == 0:
        return 0
    
    environment_variables_input = environment_variables_input.replace(" ", "")
    for env_variable in environment_variables_input.splitlines():
        if env_variable.startswith("#"):
            continue
        env_var_name, env_var_value = env_variable.split("=", 1)
        try:
            os.environ[env_var_name] = env_var_value
        except: 
            print("Failed to set env variable " + env_var_name + ".")


def import_environment_values(file_path="") -> str:
    "Read from env. var. file"
    environment_variables_input = None

    try: 
        file = open(file_path if file_path != "" else ".env", "r")
        environment_variables_input = file.read()
        file.close()
    except:
        if file_path != "":
            print("Invalid path to: environment variables file.")
            print("Attempting opening default .env file")
            environment_variables_input = import_environment_values()
        else:
            print("Default environment file abscent.")
            print("Make sure there is an .env file in root directory, or provide a path to an .env file.")
            sys.exit(1)

    return environment_variables_input