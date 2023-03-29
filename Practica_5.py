


def Read_File():
    with open("archivos.txt", "r") as file:
        lines = file.readlines()
    return lines


files = Read_File()
print(files)