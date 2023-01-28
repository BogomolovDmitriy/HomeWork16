import data_provider as dp
import logger as log


def view(name_file): # получаем данные и передаем их на обработку
    data = dp.readFile(dp.path(name_file))
    length = len(data)
    log.logger(length)
    return data

