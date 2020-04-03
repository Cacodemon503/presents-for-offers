#!/usr/bin/env python3
# coding: utf-8

import random
import base64
import json
from urllib.parse import parse_qs


def offer_cashback(name):
    if name == '':  # insert valid promocode
        lst = ['Подписка на "Okko"',
               'Подписка на "IVI"',
               'Подарочная карта "AMEDIATEKA"',
               'Подароный сертификат "Wink"',
               'Сертификат на покупку "Lamoda"',
               'Сертификат на покупку украшений "Moments"',
               'Сертификат на покупку украшений "Leski Store"',
               'Сертификат на покупку "Вeauty365"',
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
               'Подарочная карта "Клуб привилегий"']

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
