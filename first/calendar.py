day = int(input("Введите какое сегодня число"))
try:
    if day > 31:
        raise ValueError("Не бывает такого календарного числа")
        #просто создаем свой тип ошибки
except ValueError:
    print("Программа нашла неправильное значение")
finally:
    #finally у нас всегда выполняется
    print("Люблю хорошую погоду")