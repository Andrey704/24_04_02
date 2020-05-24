import os

data_file = input("Введите название файла: ")
#если файл существует, значит мы его удалим
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f"Error: {data_file} неправильное имя файла или его нет в данной директории")