# coding: utf-8

from common.card import Round

if __name__ == "__main__":
  round = Round(5, 1, 2, 3, 4)
  print("、".join(map(lambda item: str(item), round.east_cards)))
  print("、".join(map(lambda item: str(item), round.south_cards)))
  print("、".join(map(lambda item: str(item), round.west_cards)))
  print("、".join(map(lambda item: str(item), round.north_cards)))
