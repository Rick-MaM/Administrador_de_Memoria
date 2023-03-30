from msvcrt import getch
import os
option = 0

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
    
    def Primer_Ajuste(self):
        while len(self.file) != 0:
            Date = self.file[0].split(", ")
            file_size = self.Memory_Space(Date[1])
            for count_memory_space in range(len(self.memory_space)):
                if self.is_occupied(self.memory_space[count_memory_space]):
                    pass
                else:
                    available_memory = self.Memory_Space(self.memory_space[count_memory_space])
                    if file_size <= available_memory:
                        unused_memory = available_memory - file_size
                        self.memory_space[count_memory_space] = Date[0] + " (" + str(file_size) + "kb" + ")"
                        break
                if count_memory_space == len(self.memory_space) - 1:
                    print("NO hay espacio suficiente para guardar ", Date[0])
            if unused_memory != 0:
                unused_memory = str(unused_memory) + "kb"
                self.Excess_space(unused_memory, count_memory_space)
                unused_memory = 0
            self.file.pop(0)
    
    def Mejor_ajuste(self):
        while len(self.file) != 0:
            Date = self.file[0].split(", ")
            file_size = self.Memory_Space(Date[1])
            mejor_ajuste = self.Best_option(file_size)

            for count in range(len(self.memory_space)):
                if self.is_occupied(self.memory_space[count]):
                    pass
                else:
                    available_memory = self.Memory_Space(
                        self.memory_space[count])
                    if mejor_ajuste == available_memory and mejor_ajuste >= file_size:
                        unused_memory = available_memory - file_size
                        self.memory_space[count] = Date[0] + \
                            " (" + str(file_size) + "kb" + ")"
                        break
                if count == len(self.memory_space) - 1:
                    print("NO hay espacio suficiente para guardar ", Date[0])
            if unused_memory != 0:
                unused_memory = str(unused_memory) + "kb"
                self.Excess_space(unused_memory, count)

            self.file.pop(0)
    
    def Peor_ajuste(self): 
        while len(self.file) != 0:
            Date = self.file[0].split(", ")
            file_size = self.Memory_Space(Date[1])
            Peor_ajuste = self.Worse_option(file_size)
            for count in range(len(self.memory_space)):
                if self.is_occupied(self.memory_space[count]):
                    pass
                else:
                    available_memory = self.Memory_Space(self.memory_space[count])
                    if Peor_ajuste == available_memory and Peor_ajuste >= file_size:
                        unused_memory = available_memory - file_size
                        self.memory_space[count] = Date[0] + \
                            " (" + str(file_size) + "kb" + ")"
                        break
                if count == len(self.memory_space) - 1:
                    print("NO hay espacio suficiente para guardar ", Date[0])
                    
            if unused_memory != 0:
                unused_memory = str(unused_memory) + "kb"
                self.Excess_space(unused_memory, count)
                unused_memory = 0

            self.file.pop(0)

    def Siguiente_Ajuste(self):
        count_memory_space = 0
        previus_count = 0
        while len(self.file) != 0:
            Date = self.file[0].split(", ")
            file_size = self.Memory_Space(Date[1])

            while count_memory_space < len(self.memory_space):
                if self.is_occupied(self.memory_space[count_memory_space]):
                    pass
                else:
                    available_memory = self.Memory_Space(self.memory_space[count_memory_space])
                    if file_size <= available_memory:
                        unused_memory = available_memory - file_size
                        self.memory_space[count_memory_space] = Date[0] + " (" + str(file_size) + "kb" + ")"
                        self.file.pop(0)
                        break
                count_memory_space += 1

            if unused_memory != 0:
                unused_memory = str(unused_memory) + "kb"
                self.Excess_space(unused_memory, count_memory_space)
                unused_memory = 0

            if count_memory_space == len(self.memory_space):
                
                if previus_count == 0:
                    previus_count = count_memory_space
                    count_memory_space = 0
                else:
                    print("NO hay espacio suficiente para guardar ", Date[0])
                    self.file.pop(0)
                
            


def Read_File():
    with open("archivos.txt", "r") as file:
        lines = file.readlines()
    return lines

def Menu(count_option):
    if count_option == 0:
        print("-----> 1. Primer ajuste <-----")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("       Salir")

    elif count_option == 1:
        print("       1. Primer ajuste")
        print("-----> 2. Mejor ajuste <-----")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("       Salir")

    elif count_option == 2:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste ")
        print("-----> 3. Peor ajuste <-----")
        print("       4. Siguiente ajuste")
        print("       Salir")

    elif count_option == 3:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("-----> 4. Siguiente ajuste <-----")
        print("       Salir")

    elif count_option == 4:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("-----> Salir <-----")

    elif count_option >= 5:
        print("-----> 1. Primer ajuste <-----")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("       Salir")
        count_option = 0

    elif count_option < 0:
        print("       1. Primer ajuste")
        print("       2. Mejor ajuste")
        print("       3. Peor ajuste")
        print("       4. Siguiente ajuste")
        print("-----> Salir <-----")
        count_option = 4
    return count_option

def select(option):
    files = Read_File()
    memory = Memory_Management(files)
    if option == 0:
        memory.Primer_Ajuste()
        for count_memory in range(len(memory.memory_space)):
            print("|",memory.memory_space[count_memory],end="")
        print("|")
    elif option == 1:
        memory.Mejor_ajuste()
        for count_memory in range(len(memory.memory_space)):
            print("|", memory.memory_space[count_memory], end="")
        print("|")
    elif option == 2:
        memory.Peor_ajuste()
        for count_memory in range(len(memory.memory_space)):
            print("|", memory.memory_space[count_memory], end="")
        print("|")
    elif option == 3:
        memory.Siguiente_Ajuste()
        for count_memory in range(len(memory.memory_space)):
            print("|", memory.memory_space[count_memory], end="")
        print("|")


print("\nPara moverse entre opciones: s: Abajo, w: Arriba")
print("-----> 1. Primer ajuste <-----")
print("       2. Mejor ajuste")
print("       3. Peor ajuste")
print("       4. Siguiente ajuste")
print("       Salir")

while True:

    caracter = ord(getch())
    if caracter == 115:
        option += 1
    elif caracter == 119:
        option -= 1
    elif caracter == 13:
        if option == 4:
            break
        else:
            select(option)
            input("\nENTER para continuar...")
    os.system("cls")
    option = Menu(option)
