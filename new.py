import random


def offer_cashback(name):
    if name[0] == 'W' and name[1:].lower() in {'puntok'}:  # insert valid promocode
        lst = ['Подписка на "Okko"',
               'Подписка на "IVI"',
               'Подарочная карта "AMEDIATEKA"',
               'Подароный сертификат "Wink"',
               'Сертификат на покупку "Lamoda"',
               'Сертификат на покупку "Golden Apple"',
               'Подарочный сертификат "Яндекс.Плюс"',
               'Сертификат на покупку "Ozon"',
               'Сертификат на покупку "Лабиринт"',
               'Сертификат на покупку "РИВ ГОШ"',
               'Сертификат на покупку "Республика"',
               'Подарочная карта "Storytel"',
               'Подарочный сертификат "Combo от Mail.ru"',
               'Подарочный сертификат "WILDBERRIES"',
               'Подарочный сертификат "Яндекс.Еда"',
               'Подарочная карта "Клуб привилегий"',
               'Подарочный сертификат "Яндекс.Музыка"',
               'Подарочная карта Яндекс.Такси',
               'Подарочная карта "Ситимобил"',
               'Подарочная карта "Литрес"',
               'Сертификат в "Спортмастер"']

        luck = str(random.choice(lst))
        cashback = 'Твой приз: {}!'.format(luck)
        return cashback
    elif name[0] == 'M' and name[1:].lower() in {''}:
        lst = ['Подписка на "Okko"',
               'Подписка на "IVI"',
               'Подарочная карта "AMEDIATEKA"',
               'Подароный сертификат "Wink"',
               'Сертификат на покупку "Lamoda"',
               'Подарочный сертификат "Яндекс.Плюс"',
               'Сертификат на покупку "Ozon"',
               'Сертификат на покупку "Лабиринт"',
               'Сертификат на покупку "Республика"',
               'Подарочная карта "Storytel"',
               'Подарочный сертификат "Combo от Mail.ru"',
               'Подарочный сертификат "Яндекс.Еда"',
               'Подарочная карта "Клуб привилегий"',
               'Подарочный сертификат "Яндекс.Музыка"',
               'Подарочная карта Яндекс.Такси',
               'Подарочная карта "Ситимобил"',
               'Подарочная карта "Литрес"',
               'Сертификат в "Спортмастер"',
               'Сертификат на выбор в Steam, PS Store или Xbox']

        luck = str(random.choice(lst))
        cashback = 'Твой приз: {}!'.format(luck)
        return cashback
    else:
        cashback = 'Код не действителен!'
        return cashback


if __name__ == "__main__":
    name = str(input('')).replace(' ', '')
    cashback = offer_cashback(name)
    print(cashback)
