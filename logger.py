from datetime import datetime as dt

def logger(data):
    time = dt.now().strftime("%H:%M") # получаем время и переводим его в формат (час: мин)
    with open("log.csv", "a") as file: # создаем файл и записываем в него информацию (время и количество записей)
        file.write("{} - number of records: {}\n"
                    .format(time, data))