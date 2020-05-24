import shutil
import random

print("Запущена программа бекапа")
target = input("Введите название папки, которую надо забекапить")
string = ''
for i in range(len(target)):
    string += str(random.randint(0, 9))
plan_b = target+string

shutil.copytree(target, plan_b)