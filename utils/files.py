import os
import json

import click


def write_to_file(file_name: str, content: list[str]):
    try:
        with open("./" + file_name, 'a') as file:
            for line in content:
                file.write(line + "\n")

            file.close()
    except FileNotFoundError:
        path: list[str] = file_name.split("/")
        
        for i in range(len(path) - 1):
            os.mkdir(path[i])
            os.chdir(path[i])

        with open("./" + path[-1], 'a') as file:
            for line in content:
                file.write(line + "\n")

            file.close()


def write_to_json(file_name: str, content: list[str]):
    if "." in file_name and file_name.split(".")[-1] != "json": raise click.UsageError("'--json' precisa receber um arquivo .json")

    if "." not in file_name: file_name = file_name + ".json"

    data: dict[str, list[str]] = { "data": content }

    json_object: str = json.dumps(data, indent = 4)

    try:
        with open("./" + file_name, 'a') as file:
            file.write(json_object)

            file.close()
    except FileNotFoundError:
        path: list[str] = file_name.split("/")
        
        for i in range(len(path) - 1):
            os.mkdir(path[i])
            os.chdir(path[i])

        with open("./" + path[-1], 'a') as file:
            file.write(json_object)

            file.close()
