# coding: utf-8

from .card import CardItem
from .mode import CardMode

def test_three():
    a = [CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.THREE

    a = [CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.INVALID

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.THREE

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
    assert mode == CardMode.STRAIGHT_FLUSH

    a = [CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.CLUB, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.CLUB, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(4, CardItem.DIAMOND, 2),
         CardItem(4, CardItem.DIAMOND, 3),
         CardItem(4, CardItem.CLUB, 4),
         CardItem(4, CardItem.DIAMOND, 5),
         CardItem(4, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(4, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(5, CardItem.DIAMOND, 2),
         CardItem(5, CardItem.DIAMOND, 3),
         CardItem(5, CardItem.CLUB, 4),
         CardItem(5, CardItem.DIAMOND, 5),
         CardItem(5, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(5, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(14, CardItem.DIAMOND, 2),
         CardItem(14, CardItem.DIAMOND, 3),
         CardItem(14, CardItem.CLUB, 4),
         CardItem(14, CardItem.DIAMOND, 5),
         CardItem(14, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(14, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(8, CardItem.DIAMOND, 2),
         CardItem(8, CardItem.DIAMOND, 3),
         CardItem(8, CardItem.CLUB, 4),
         CardItem(8, CardItem.DIAMOND, 5),
         CardItem(8, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(8, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(2, CardItem.CLUB, 2),
         CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.STRAIGHT_FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 7),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.STRAIGHT_FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.STRAIGHT_FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 4),
         CardItem(2, CardItem.CLUB, 5),
         CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.CLUB, 5),
         CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(8, CardItem.HEART, 8),
         CardItem(8, CardItem.HEART, 8),
         CardItem(8, CardItem.CLUB, 5),
         CardItem(8, CardItem.DIAMOND, 2),
         CardItem(8, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(8, a)
    assert mode == CardMode.FLUSH

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
    assert mode == CardMode.FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.DIAMOND, 6),
         CardItem(2, CardItem.DIAMOND, 8),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.STRAIGHT_FLUSH

    a = [CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 2),
         CardItem(2, CardItem.HEART, 6),
         CardItem(2, CardItem.DIAMOND, 9),
         CardItem(2, CardItem.DIAMOND, 10),
         ]
    mode = CardMode.get_card_mode(2, a)
    assert mode == CardMode.FLUSH

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
