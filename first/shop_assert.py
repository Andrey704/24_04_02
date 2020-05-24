#положим, что нам нужно создать функцию, которая не разрешает
# нам делать отрицательные ценники, иначе нам придется доплачить покупателю

def apply_discount(product, discount):
    """ Принимаем на вход данные о товаре в виде словаря и скидку"""
    price = int(product['цена'] * (1.0 - discount))
    try:
        assert 0 <= price <=product['цена']
        #запрещает отрицательную и больше изначальной цены
    except AssertionError:
        print("Что у тебя с цифрами гений?")
    else:
        return price, product['имя']

kreslo = {'имя': 'кресло', 'цена': 3600}
# объявляем скидку в 25%
print(apply_discount(kreslo, 0.25))

print(apply_discount(kreslo, 2.25))