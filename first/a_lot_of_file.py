def count_word(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        # print("Нет тут файлика с именем" + filename)
        pass
        #просто промолчим в ответ
    else:
        amount_of_symbols = 0  # пустую переменную для подсчета символов
        words = contents.split('. ')  # разбивает в список все слова
        for word in words:
            amount_of_symbols += len(word)  # прибавляем длину каждого слова в списке
        num_words = len(words)  # считаем сколько всего слов у нас используется
        print(f"в {filename} всего {amount_of_symbols} слов в символах")
        print(f"в файлике {filename} находится {num_words} слов")
        print(
            f"средняя длина слова в {filename} это {round(amount_of_symbols / num_words)}")
        print(words)


spi_file = ['evgini-onegin.txt', 'prestuplenie-i-nakaznia.txt',
            'voyna-i-mir.txt']

for file in spi_file:
    count_word(file)
