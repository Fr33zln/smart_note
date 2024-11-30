import json
import os #зєдання звязків

def write_json(name_file,data):
    abs_path = os.path.abspath(__file__ + "/..") #абсолютний шлях до файлу - "/.." - видалення останнього елементу файлу тобто щоб не заходило в крафт джсон
    os.chdir(abs_path) #віртуально заходимо в файл
    with open(os.path.join(abs_path, name_file), "w", encoding= "utf-8") as file:
        json.dump(data,file, indent = 4, ensure_ascii= False)
#автоматично знаходить шляхи до файлу без його назви і його стисняє в одне ціле

def read_json(name_file):
    abs_path = os.path.abspath(__file__ + "/..")
    with open(os.path.join(abs_path, name_file), "r", encoding= "utf-8") as file:
        data = json.load(file)
    return data