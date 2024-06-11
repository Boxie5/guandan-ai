# coding: utf-8

from .card import CardItem
from .mode import CardMode

def test_vvmode():
    a = [CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.CLUB, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 9),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 8),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)
