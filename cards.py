# -*-coding:utf-8-*-
from __future__ import unicode_literals

'''
card id starts from 1, and 0 for empty card
'''
class Cards:

    def __init__(self):
        pass

    '''
    return card description (to send to client)
    card_id: int
    '''
    def description(self, card_id):
        pass

    '''
    return result for match between cards1 and cards2
    cards1: list[card_id]
    cards2: list[card_id]
    '''
    def match(cards1, cards2):
        pass
