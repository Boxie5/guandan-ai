# coding: utf-8

from .card import CardItem

class CardMode():
    SINGLE = 1 # 单张
    TWO = 2 # 对子
    THREE = 3 # 三不带
    THREE_WITH_TWO = 4 # 三带二
    THREE_TWO = 5 # 三连对
    TWO_THREE = 6 # 钢板
    FIVE = 7 # 杂顺p
    COLOR_FIVE = 8 # 同花顺
    FOUR_BOOM = 9 # 四炸
    FIVE_BOOM = 10 # 五炸
    SIX_BOOM = 11 # 六炸
    SEVEN_BOOM = 12 # 七炸
    EIGHT_BOOM = 13 # 八炸
    KING_BOOM = 14 # 天王炸

    INVALID = 99 # 不合法的

    def __init__(self) -> None:
        pass

    @classmethod
    def get_card_mode(self, general, cards, prefer_mode = INVALID):
        cards.sort()
        print("、".join(map(lambda item: str(item), cards)))
        card_len = len(cards)

        taylor_swift_count = 0
        plain_cards = []
        for c in cards:
            if c.is_taylor_swift():
                taylor_swift_count += 1
            else:
                plain_cards.append(c)

        if card_len == 1:
            return CardMode.SINGLE
        elif card_len == 2:
            if cards[0].rank == cards[1].rank:
                return CardMode.TWO
            elif cards[0].is_taylor_swift() or cards[1].is_taylor_swift():
                return CardMode.TWO
            else:
                return CardMode.INVALID
        elif card_len == 3:
            if taylor_swift_count == 2:
                return CardMode.THREE
            elif taylor_swift_count == 1:
                if CardMode.get_card_mode(general, plain_cards) == CardMode.TWO:
                    return CardMode.THREE
                else:
                    return CardMode.INVALID
            elif cards[0].rank == cards[1].rank and cards[0].rank == cards[2].rank:
                return CardMode.THREE
            else:
                return CardMode.INVALID
        elif card_len == 4:
            if taylor_swift_count == 2:
                if CardMode.get_card_mode(general, plain_cards) == CardMode.TWO:
                    return CardMode.FOUR_BOOM
                else:
                    return CardMode.INVALID
            elif taylor_swift_count == 1:
                if CardMode.get_card_mode(general, plain_cards) == CardMode.THREE:
                    return CardMode.FOUR_BOOM
                else:
                    return CardMode.INVALID
            elif cards[0].rank == cards[1].rank and cards[0].rank == cards[2].rank and cards[0].rank == cards[3].rank:
                return CardMode.FOUR_BOOM
            # 天王炸
            elif cards[0].rank == 16 and cards[1].rank == 16 and cards[2].rank == 17 and cards[3].rank == 17:
                return CardMode.KING_BOOM
            else :
                return CardMode.INVALID
        elif card_len == 5:
            if taylor_swift_count == 0:
                if cards[0].rank == cards[4].rank:
                    return CardMode.FIVE_BOOM
                elif cards[0].rank == cards[2].rank and cards[3].rank == cards[4].rank:
                    return CardMode.THREE_WITH_TWO
                elif cards[0].rank == cards[1].rank and cards[2].rank == cards[4].rank:
                    return CardMode.THREE_WITH_TWO
                elif cards[4].rank == 14: # 有A的顺子
                    if cards[0].rank == 2 and cards[1].rank == 3 and cards[2].rank == 4 and cards[3].rank == 5:
                        if cards[0].suit == cards[1].suit and cards[0].suit == cards[2].suit and cards[0].suit == cards[3].suit and cards[0].suit == cards[4].suit:
                            return CardMode.COLOR_FIVE
                        else:
                            return CardMode.FIVE
                    else:
                        return CardMode.INVALID
                elif cards[0].rank + 1 == cards[1].rank and cards[1].rank + 1 == cards[2].rank and cards[2].rank + 1 == cards[3].rank and cards[3].rank + 1 == cards[4].rank:
                    if cards[0].suit == cards[1].suit and cards[0].suit == cards[2].suit and cards[0].suit == cards[3].suit and cards[0].suit == cards[4].suit:
                        return CardMode.COLOR_FIVE
                    else:
                        return CardMode.FIVE
                else:
                    return CardMode.INVALID
            elif taylor_swift_count == 1:
                if plain_cards[0].rank == plain_cards[3].rank:
                    return CardMode.FIVE_BOOM
                elif plain_cards[0].rank == plain_cards[1].rank and plain_cards[2] == plain_cards[3].rank:
                    return CardMode.THREE_WITH_TWO
                elif plain_cards[0].rank == plain_cards[2].rank and plain_cards[3].rank < 15: # 目前假设王不能做三带二的配牌
                    return CardMode.THREE_WITH_TWO
                elif plain_cards[1].rank == plain_cards[3].rank:
                    return CardMode.THREE_WITH_TWO
                elif plain_cards[3].rank - plain_cards[0].rank == 4: # 配牌在中间的顺子
                    if plain_cards[0].rank != plain_cards[1].rank and plain_cards[1].rank != plain_cards[2].rank and plain_cards[2].rank != plain_cards[3].rank:
                        if plain_cards[0].suit == plain_cards[1].suit and plain_cards[0].suit == plain_cards[2].suit and plain_cards[0].suit == plain_cards[3].suit:
                            return CardMode.COLOR_FIVE
                        else:
                            return CardMode.FIVE
                    else:
                        return CardMode.INVALID
                elif plain_cards[3].rank - plain_cards[0].rank == 3: # 配牌在旁边的顺子
                    if plain_cards[0].rank != plain_cards[1].rank and plain_cards[1].rank != plain_cards[2].rank and plain_cards[2].rank != plain_cards[3].rank:
                        if plain_cards[0].suit == plain_cards[1].suit and plain_cards[0].suit == plain_cards[2].suit and plain_cards[0].suit == plain_cards[3].suit:
                            return CardMode.COLOR_FIVE
                        else:
                            return CardMode.FIVE
                    else:
                        return CardMode.INVALID
            elif taylor_swift_count == 2:
                if plain_cards[0].rank == plain_cards[2].rank:
                    return CardMode.FIVE_BOOM
                elif plain_cards[0].rank == plain_cards[1].rank and plain_cards[0].rank != plain_cards[2].rank:
                    return CardMode.THREE_WITH_TWO
                elif plain_cards[0].rank != plain_cards[1].rank and plain_cards[1].rank == plain_cards[2].rank:
                    return CardMode.THREE_WITH_TWO
                elif plain_cards[2].rank - plain_cards[0].rank < 5:
                    if plain_cards[0].suit == plain_cards[1].suit and plain_cards[0].suit == plain_cards[2].suit:
                        return CardMode.COLOR_FIVE
                    else:
                        return CardMode.FIVE
                # 带A的顺子还就没有处理
                return CardMode.INVALID
        elif card_len == 6:
            # TODO 有A的三联对和钢板
            if taylor_swift_count == 0:
                # 三联对
                if plain_cards[0].rank == plain_cards[1].rank \
                    and plain_cards[1].rank != plain_cards[2].rank \
                        and plain_cards[2].rank == plain_cards[3].rank \
                            and plain_cards[3].rank != plain_cards[4].rank \
                                and plain_cards[4].rank == plain_cards[5].rank:
                    if plain_cards[0].rank + 2 == plain_cards[4].rank:
                        return CardMode.THREE_TWO
                    else:
                        return CardMode.INVALID
                # 钢板
                elif plain_cards[0].rank == plain_cards[1].rank \
                    and plain_cards[1].rank == plain_cards[2].rank \
                    and plain_cards[2].rank != plain_cards[3].rank \
                    and plain_cards[3].rank == plain_cards[4].rank \
                    and plain_cards[4].rank == plain_cards[5].rank:
                    if plain_cards[0].rank + 1 == plain_cards[5].rank:
                        return CardMode.TWO_THREE
                    else:
                        return CardMode.INVALID
                # 六炸
                elif plain_cards[0].rank == plain_cards[5].rank:
                    return CardMode.SIX_BOOM
            elif taylor_swift_count == 1:
                # 三联对
                if plain_cards[0].rank + 2 == plain_cards[4].rank:
                    if plain_cards[1].rank != plain_cards[2].rank or plain_cards[2].rank != plain_cards[3].rank:
                        return CardMode.THREE_TWO
                    else:
                        return CardMode.INVALID
                # 钢板
                if plain_cards[0].rank + 1 == plain_cards[4].rank:
                    if plain_cards[1].rank != plain_cards[2].rank or plain_cards[2].rank != plain_cards[3].rank:
                        return CardMode.TWO_THREE
                    else:
                        return CardMode.INVALID
                # 六炸
                if plain_cards[0].rank == plain_cards[4].rank:
                    return CardMode.SIX_BOOM
            elif taylor_swift_count == 2:
                # 三联对
                if plain_cards[0].rank + 2 == plain_cards[3].rank:
                    if plain_cards[1].rank != plain_cards[2].rank or plain_cards[2].rank != plain_cards[3].rank:
                        return CardMode.THREE_TWO
                    else:
                        return CardMode.INVALID
                # 钢板
                if plain_cards[0].rank + 1 == plain_cards[3].rank:
                    if plain_cards[1].rank != plain_cards[2].rank or plain_cards[2].rank != plain_cards[3].rank:
                        return CardMode.TWO_THREE
                    else:
                        return CardMode.INVALID
                # 六炸
                if plain_cards[0].rank == plain_cards[3].rank:
                    return CardMode.SIX_BOOM
        elif card_len == 7:
            if taylor_swift_count == 0:
                if plain_cards[0].rank == plain_cards[6].rank:
                    return CardMode.SEVEN_BOOM
                else:
                    return CardMode.INVALID
            elif taylor_swift_count == 1:
                if plain_cards[0].rank == plain_cards[5].rank:
                    return CardMode.SEVEN_BOOM
                else:
                    return CardMode.INVALID
            elif taylor_swift_count == 2:
                if plain_cards[0].rank == plain_cards[4].rank:
                    return CardMode.SEVEN_BOOM
                else:
                    return CardMode.INVALID
        elif card_len == 8:
            if taylor_swift_count == 0:
                if plain_cards[0].rank == plain_cards[7].rank:
                    return CardMode.EIGHT_BOOM
                else:
                    return CardMode.INVALID
            elif taylor_swift_count == 1:
                if plain_cards[0].rank == plain_cards[6].rank:
                    return CardMode.EIGHT_BOOM
                else:
                    return CardMode.INVALID
            elif taylor_swift_count == 2:
                if plain_cards[0].rank == plain_cards[5].rank:
                    return CardMode.EIGHT_BOOM
                else:
                    return CardMode.INVALID
        else:
            return CardMode.INVALID

        return CardMode.INVALID
