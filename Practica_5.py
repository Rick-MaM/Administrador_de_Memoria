
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
    
    def Excess_space(self, kilobytes, position):
        list_aux = self.memory_space
        self.memory_space = []
        for count in range(len(list_aux)):
            if count == position:
                self.memory_space.append(kilobytes)
            self.memory_space.append(list_aux[count])
        print(self.memory_space)

    def is_occupied(self, space):
        if "." in space:
            return True
        else:
            return False
        
    def sort_memory(self):
        new_list = []
        for count in range(len(self.memory_space)):
            if self.is_occupied(self.memory_space[count]):
                pass
            else:
                kilobytes = self.Memory_Space(self.memory_space[count])
                new_list.append(kilobytes)
        new_list.sort()
        return new_list[len(new_list)-1]
    
    def Best_option(self, file_size):
        mejor_ajuste = self.sort_memory()
        for count_memory_space in range(len(self.memory_space)):
            if self.is_occupied(self.memory_space[count_memory_space]):
                pass
            else:
                memory = self.Memory_Space(
                    self.memory_space[count_memory_space])
                if memory >= file_size and memory < mejor_ajuste:
                    mejor_ajuste = memory
        return mejor_ajuste

    def Worse_option(self, file_size):
        Peor_ajuste = self.sort_memory()
        for count_memory_space in range(len(self.memory_space)):
            if self.is_occupied(self.memory_space[count_memory_space]):
                pass
            else:
                memory = self.Memory_Space(
                    self.memory_space[count_memory_space])
                if memory >= file_size and memory > Peor_ajuste:
                    Peor_ajuste = memory
        return Peor_ajuste


def Read_File():
    with open("archivos.txt", "r") as file:
        lines = file.readlines()
    return lines


files = Read_File()
memory = Memory_Management(files)

print(memory.Best_option(500), memory.Worse_option(500))
