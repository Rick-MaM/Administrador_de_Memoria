
class Memory_Management:
    def __init__(self, file):
        self.memory_space = ['1000kb', '400kb', '1800kb','700kb', '900kb', '1200kb', '1500kb']
        self.file = file

    def Memory_Space(self, kb):
        kilobytes = ''
        for count_kb in kb:
            if count_kb == 'k':
                return int(kilobytes)
            else:
                kilobytes = kilobytes + count_kb


def Read_File():
    with open("archivos.txt", "r") as file:
        lines = file.readlines()
    return lines


files = Read_File()
memory = Memory_Management(files)

print(memory.Memory_Space("1000kb"))
