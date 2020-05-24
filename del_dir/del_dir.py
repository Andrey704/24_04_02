import os
import shutil

while True:
    move = input("Y - создать папку, N - удалить папку, q - прекратить")
    if move == 'Y':
        make_dir = input("Введите название директории")
        try:
            os.mkdir(make_dir)
        except FileExistsError:
            print("Уже есть такая папка!")
        else:
            print(f"я сделаль {make_dir}")
    elif move == "N":
        del_dir = input("Введите директорию, которую вы хотите удалить")
        shutil.rmtree(del_dir)
        print(f"я удалил {del_dir}")
    elif move == 'q':
        exit()