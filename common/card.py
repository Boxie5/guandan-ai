# coding: utf-8

import random

class CardItem():
  CLUB = 2
  DIAMOND = 4
  HEART = 8
  SPADE = 16

  SUIT_MAP = {
      2  : '♣',
      4  : '♦',
      8  : '♥',
      16 : '♠'
  }

  RANK_MAP = {
      2  :  '2',
      3  :  '3',
      4  :  '4',
      5  :  '5',
      6  :  '6',
      7  :  '7',
      8  :  '8',
      9  :  '9',
      10 : 'T',
      11 : 'J',
      12 : 'Q',
      13 : 'K',
      14 : 'A',
      16: 'LG',
      17: 'BG'
  }

  suit = 2
  rank = 2
  general = 2

  def __init__(self, general, suit, rank):
    self.general = general
    self.suit = suit
    self.rank = rank

  def is_taylor_swift(self):
    return self.rank == self.general and self.suit == CardItem.HEART

  def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank

  def __lt__(self, other):
    selfrank = self.rank if self.rank != self.general else 15
    otherrank = other.rank if other.rank != self.general else 15
    return selfrank < otherrank or (selfrank == otherrank and self.suit < other.suit)

  def __le__(self, other):
    selfrank = self.rank if self.rank != self.general else 15
    otherrank = other.rank if other.rank != self.general else 15
    return selfrank < otherrank or (selfrank == otherrank and self.suit == other.suit)

  def __gt__(self, other):
    selfrank = self.rank if self.rank != self.general else 15
    otherrank = other.rank if other.rank != self.general else 15
    return selfrank > otherrank or (selfrank == otherrank and self.suit > other.suit)

  def __ge__(self, other):
    selfrank = self.rank if self.rank != self.general else 15
    otherrank = other.rank if other.rank != self.general else 15
    return selfrank > otherrank or (selfrank == otherrank and self.suit == other.suit)

  def __str__(self):
    if self.rank > 14:
      return CardItem.RANK_MAP[self.rank]
    else:
      return "{}{}".format(CardItem.SUIT_MAP[self.suit], CardItem.RANK_MAP[self.rank])

class Round():
  general = 2
  east_rank = 1
  south_rank = 2
  west_rank = 3
  north_rank = 4
  east_cards = []
  south_cards = []
  west_cards = []
  north_cards = []

  def __init__(self, general, east_rank, south_rank, west_rank, north_rank):
    self.general = general
    self.east_rank = east_rank
    self.south_rank = south_rank
    self.west_rank = west_rank
    self.north_rank = north_rank

    cards = self.__generate_cards__()
    self.east_cards = cards[:27]
    self.east_cards.sort()
    self.south_cards = cards[27:54]
    self.south_cards.sort()
    self.west_cards = cards[54:81]
    self.west_cards.sort()
    self.north_cards = cards[81:]
    self.north_cards.sort()

  def __generate_cards__(self):
    cards_left = []
    for rank in CardItem.RANK_MAP:
      if rank < 15:
        for suit in CardItem.SUIT_MAP:
          cards_left.append(CardItem(self.general, suit, rank))
          cards_left.append(CardItem(self.general, suit, rank))
      else:
        cards_left.append(CardItem(general=self.general, suit=CardItem.CLUB, rank=rank))
        cards_left.append(CardItem(general=self.general, suit=CardItem.CLUB, rank=rank))

    random.shuffle(cards_left)
    return cards_left

