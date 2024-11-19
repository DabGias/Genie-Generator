import os


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
