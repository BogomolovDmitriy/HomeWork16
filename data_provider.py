import os

def path(name_file): # определяем путь к файлу
    path = os.path.abspath(name_file) 
    return path

def readFile(file): # считываем данные с файла
    data = open(file, "r")
    line = list(i for i in data)
    data.close()
    return line

