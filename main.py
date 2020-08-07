#!/usr/bin/env python3
# coding: utf-8

import random
import base64
import json
from urllib.parse import parse_qs
import smtplib
from email.mime.text import MIMEText

def email_notification(name, cashback):
    from_who = 'XXX@gmail.com'
    to = 'XXX@'
    if cashback != 'Код не действителен!':
        msg = MIMEText(f'Code: {name} \nPresent: {cashback}')
        msg['Subject'] = 'New valid action'
    else:
        msg = MIMEText(f'Code: {name} \nПОПЫТКА НЕСАНКЦИОНИРОВАННОГО ДОСТУПА')
        msg['Subject'] = 'Unauthorized action'
    msg['From'] = from_who
    msg['To'] = to

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('XXX@gmail.com', 'XXX')
    smtpObj.sendmail(from_who, to, msg.as_string())
    smtpObj.quit()

def offer_cashback(name):
    
    if name[0].lower() == 'w' and name[1:].lower() in {'', ''}:  # insert valid promocodes
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
    elif name[0].lower() == 'm' and name[1:].lower() in {'', ''}: # insert valid promocodes
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


def handler(event, context):
    name = None
    if 'queryStringParameters' in event and 'name' in event['queryStringParameters']:
        name = event['queryStringParameters']['name']

    body = None
    if name is None:
        if event['httpMethod'] == 'POST' or \
           event['httpMethod'] == 'PUT':
            if event['isBase64Encoded']:
                body = base64.b64decode(event['body']).decode('utf-8')
            else:
                body = event['body'].decode('utf-8')

            bodydict = parse_qs(body)

            name = bodydict['name'][0] if 'name' in bodydict else None

    if name is None:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'isBase64Encoded': False,
            'body': json.dumps({
                "error": "Заполните поле с кодом"
            }, ensure_ascii=False)
        }

    name = name.strip()

    cashback = offer_cashback(name)
    email_notification(name, cashback)

    return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
            },
            'isBase64Encoded': False,
            'body': json.dumps({
                "message": cashback
            }, ensure_ascii=False)
        }
