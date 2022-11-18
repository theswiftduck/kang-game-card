import random

CARDS = {'A1':1, 'A2':2, 'A3':3, 'A4':4, 'A5':5, 'A6':6, 'A7':7, 'A8':8, 'A9':9, 'AX':10, 'AJ':10, 'AQ':10, 'AK':10,
        'B1':1, 'B2':2, 'B3':3, 'B4':4, 'B5':5, 'B6':6, 'B7':7, 'B8':8, 'B9':9, 'BX':10, 'BJ':10, 'BQ':10, 'BK':10,
        'C1':1, 'C2':2, 'C3':3, 'C4':4, 'C5':5, 'C6':6, 'C7':7, 'C8':8, 'C9':9, 'CX':10, 'CJ':10, 'CQ':10, 'CK':10,
        'D1':1, 'D2':2, 'D3':3, 'D4':4, 'D5':5, 'D6':6, 'D7':7, 'D8':8, 'D9':9, 'DX':10, 'DJ':10, 'DQ':10, 'DK':10}

class Player:
    def __init__(self, name, order):
        self.name = name
        self.order = order
        self.cards = []
        self.cards_amount = len(self.cards)

    def get_card(self, pop_card):
        self.cards.append(pop_card)

    def drop_card(self, drop_card):
        self.cards.remove(drop_card)

    def draw_card(self, pop_card):
        self.cards.append(pop_card)

    def check_score(self):
        score = 0
        for i, card in enumerate(self.cards):
            score += CARDS[card]
        return score




class Deck:
    def __init__(self):
        self.cards = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'AX', 'AJ', 'AQ', 'AK',
                       'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BX', 'BJ', 'BQ', 'BK',
                       'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'CX', 'CJ', 'CQ', 'CK',
                       'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DX', 'DJ', 'DQ', 'DK']

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def pop(self):
        pop_card = self.cards[-1]
        self.cards.pop()
        return pop_card

class Table:
    def __init__(self):
        self.on_table = ''

