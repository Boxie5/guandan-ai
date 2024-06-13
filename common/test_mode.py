# coding: utf-8

from .card import CardItem
from .mode import CardMode

def test_four():
    a = [CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FOUR_BOOM

    a = [CardItem(2, CardItem.HEART, 16),
         CardItem(2, CardItem.HEART, 16),
         CardItem(2, CardItem.HEART, 17),
         CardItem(2, CardItem.HEART, 17),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.KING_BOOM

def test_five():
    a = [CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.COLOR_FIVE

    a = [CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.CLUB, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FIVE

#     a = [CardItem(2, CardItem.DIAMOND, 2),
#          CardItem(2, CardItem.DIAMOND, 3),
#          CardItem(2, CardItem.CLUB, 4),
#          CardItem(2, CardItem.DIAMOND, 5),
#          CardItem(2, CardItem.DIAMOND, 14),
#          ]
#     mode = CardMode.get_card_mode(2, a)
#     assert mode == CardMode.FIVE

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.COLOR_FIVE

    a = [CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.THREE_WITH_TWO

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FIVE_BOOM

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FIVE

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FIVE

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.COLOR_FIVE

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 9),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FIVE

def test_six():
    a = [CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.INVALID

    a = [CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.TWO_THREE

    a = [CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.THREE_TWO

    a = [CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 8),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.INVALID

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.THREE_TWO

def test_seven():
    a = [CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.SPADE, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.SEVEN_BOOM

    a = [CardItem(2, CardItem.HEART, 4),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.SPADE, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.INVALID

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.SPADE, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.SEVEN_BOOM


    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.SPADE, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.SEVEN_BOOM

def test_eight():
    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 3),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.SPADE, 6),
         CardItem(2, CardItem.SPADE, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.INVALID

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.CLUB, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.SPADE, 6),
         CardItem(2, CardItem.SPADE, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.EIGHT_BOOM
