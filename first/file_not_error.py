

filename = input("Введите название файла, который хотите прочитать")
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    print("Да нет тут файла с именем" + filename)
