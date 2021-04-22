import sys


class Entry:

    def __init__(self, data):
        self.data = data

    def read(self, data):
        inp = input("Ввод данных из file, console: ")
        while not (inp == "console" or inp == "file"):
            inp = input("Ввод данных из file, console: ")
        if inp == "console":
            self.read_from_console(data)
        else:
            self.read_from_file(data)

    def read_from_console(self, data):
        while True:
            try:
                n = int(input("Введите количество точек: "))
                break
            except ValueError:
                print("Некорректный ввод данных")
        data.set_n(n)

        for i in range(len(0, n)):
            while True:
                try:
                    number = float(input("Введите значение x" + i + ": "))
                    break
                except ValueError:
                    print("Некорректный ввод данных")
            data.set_element_mass(number, 0, i)
            while True:
                try:
                    number = float(input("Введите значение y" + i + ": "))
                    break
                except ValueError:
                    print("Некорректный ввод данных")
            data.set_element_mass(number, 1, i)

        file_or_console = input("Вывод данных в file, console: ")
        while not (file_or_console == "file" or file_or_console == "console"):
            file_or_console = input("Вывод данных в file, console: ")
        data.set_file_or_console(file_or_console)

    def read_from_file(self, data):
        file = open("resources/input.txt")

        try:
            n = float(file.readline().strip())
        except ValueError as e:
            print("Exception:", e)
            sys.exit()

        mass = file.readline().strip().replace(",", ".").split(" ")
        for i in range(len(0, n)):
            try:
                number = float(mass[i])
            except ValueError as e:
                print("Exception :", e)
                sys.exit()
            data.set_element_mass(number, 0, i)

        mass = file.readline().strip().replace(",", ".").split(" ")
        for i in range(len(0, n)):
            try:
                number = float(mass[i])
            except ValueError as e:
                print("Exception :", e)
                sys.exit()
            data.set_element_mass(number, 1, i)

        try:
            file_or_console = file.readline().strip()
            if not (file_or_console == "file" or file_or_console == "console"):
                raise Exception("Неверно введен данные связанные с выводом информации")
        except Exception as e:
            print("Exception:", e)
            sys.exit()
        data.set_file_or_console(file_or_console)