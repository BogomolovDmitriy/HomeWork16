path = "guid.txt"

# def get_data(path):
#     data = open(path, "r")
#     line_data = list(i for i in data)
#     data.close()
#     return line_data

# print(get_data(path))

data = open(path, "r")
for line in data:
    print(line)
data.close()