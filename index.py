# coding: utf-8

from common.card import Round, CardItem
from common.mode import CardMode

if __name__ == "__main__":
#   round = Round(5, 1, 2, 3, 4)
#   print("、".join(map(lambda item: str(item), round.east_cards)))
#   print("、".join(map(lambda item: str(item), round.south_cards)))
#   print("、".join(map(lambda item: str(item), round.west_cards)))
#   print("、".join(map(lambda item: str(item), round.north_cards)))

    a = [CardItem(2, CardItem.DIAMOND, 2),
         CardItem(2, CardItem.DIAMOND, 3),
         CardItem(2, CardItem.CLUB, 4),
         CardItem(2, CardItem.DIAMOND, 5),
         CardItem(2, CardItem.DIAMOND, 14),
         ]
    mode = CardMode.get_card_mode(2, a)
    print(mode)
