# -*-coding:utf-8-*-
from __future__ import unicode_literals
import requests as r
import utility as ut
from models import *

class GameValue:

    def __init__(self):
        self.energy = 0
        self.magic = 0
        self.score = 0

    def clear(self):
        self.energy = 0
        self.magic = 0
        self.score = 0

    def get(self):
        return self.__dict__

    '''
    set value, data is json pkg
    data: dict{str:num}
    '''
    def set(data):
        self.energy = data["energy"]
        self.magic = data["magic"]
        self.score = data["score"]

class GameCards:

    def __init__(self):
        self.pool = [0]*8
        self.board = [0]*3

    def clear(self):
        self.pool = [0]*8
        self.board = [0]*3

    def get(self):
        return self.__dict__

    '''
    set value, data is json pkg
    data: dict{str:list[num]}
    '''
    def set(data):
        self.pool = data["pool"]
        self.board = data["board"]


class Game:

    '''
    _user_id: int: user id
    _url: str: server url
    _status_code: int: status code
    _res: dict{str:str/int}: last response json from server
    game_value: class GameValue:
    '''
    def __init__(self, server_url, user_id):
        self._url = server_url
        self._user_id = user_id
        self._status_code = 0
        self._res = None
        self.game_value = GameValue()
        self.game_cards = GameCards()
        self._handle = [
            self._handle_0,
            self._handle_1,
            self._handle_2,
            self._handle_3,
            self._handle_4,
            self._handle_5,
            self._handle_6
        ]
        self._jump = [
            self._jump_0,
            self._jump_1,
            self._jump_2,
            self._jump_3,
            self._jump_4,
            self._jump_5,
            self._jump_6
        ]


    '''
    handle_num: handle function for status_code = num, return data that's to send to server
    rtype: dict
    '''
    def _handle_0(self):
        return {
            "statusCode": 0,
            "userId": self._user_id
        }

    def _handle_1(self):
        print "user id: " + str(self._user_id)
        print "all ur cards:"

        # print all cards
        print res["cards"]

        card_ids = raw_input("please select 8 cards (type ids seperated by space):")
        ids = ut.seperate_nums(ids)
        while True:
            if list_in_list(ids, res["cards"]):
                break
            print "Invalid card id, which is not your cards"
            card_ids = raw_input("please select 8 cards (type ids seperated by space):")
            ids = ut.seperate_nums(ids)
        self.game_cards.pool = ids
        return {
            "statusCode": 1,
            "userId": self._user_id,
            "cards": self.game_cards.get()
        }

    def _handle_2(self):
        return {
            "statusCode": 2
            "userId": self._user_id,
            "value": self.game_value.get()
        }

    #TODO: set interval
    def _handle_3(self):
        print "question:" + res["question"]
        # start timer
        answer = raw_input("your answer:")
        return {
            "statusCode": 3
            "userId": self._user_id,
            "answer": answer,
            "value": self.game_value.get()
        }

    #TODO: set interval
    def _handle_4(self):
        print "Duel!"

        #set timer
        card_ids = raw_input("select 3 cards you want to put on board (type ids seperated by space):")
        ids = ut.seperate_nums(ids)
        while True:
            if list_in_list(ids, self.game_cards.pool):
                break
            print "Invalid card id, which is not in your pool"
            card_ids = raw_input("select 3 cards you want to put on board (type ids seperated by space):")
            ids = ut.seperate_nums(ids)
        self.game_cards.board = ids
        return {
            "statusCode": 4,
            "userId": self._user_id,
            "cards": self.game_cards.get(),
            "value": self.game_value.get()
        }

    def _handle_5(self):
        return {
            "statusCode": 5,
            "userId": self._user_id
        }

    def _handle_6(self):
        pass

    '''
    jump_num: jump function for status_code = num, return next status code
    rtype: int
    '''
    def _jump_0(self):
        '''
        res["card"]: list[num], size = number of all cards user has
        '''
        if res["code"] == 0:
            return 1
        else:
            print "status 0 init: receive error game code:" + str(res["code"])
            raise GameCodeError()

    def _jump_1(self):
        if res["code"] == 1:
            return 2
        elif res["code"] == 0:
            return 3
        else:
            print "status 1 preparation: receive error game code:" + str(res["code"])
            raise GameCodeError()

    def _jump_2(self):
        return self._jump_1()

    def _jump_3(self):
        if res["code"] == 0:
            self.game_value.set(res["value"])
            print "Great, you're right!" id res["isRight"] else "Sorry, you're wrong!"
            return 4
        else:
            raise GameCodeError()

    def _jump_4(self):
        if res["code"] == 1:
            return 5
        elif: res["code"] == 0:
            self.game_value.set(res["value"])
            print "You Win" if res["win"] else "You Lose"
            return 2iio
        else:
            raise GameCodeError()

    def _jump_5(self):
        return self._jump_4()

    def _jump_6(self):
        pass


    '''
    handle response and turn into another status_code
    '''
    def jump(self):
        self._status_code = self._jump[self._status_code]()

    '''
    send message to server, by status_code, return json
    '''
    def request(self, data):
        try:
            res = r.post(self._url, json=data)
        except:
            raise
        if res.status_code is not 200:
            raise HTTPCodeError()
        return res.json()

    '''
    handle last response, by status_code
    '''
    def handle(self):
        data = self._handle[self._status_code]()
        res = self.send(data)

    def isEnd(self):
        if self._res["code"] == 3:
            return True
        return False

    def run(self):
        while True:
            self._res = self.handle()
            if self.isEnd():
                break
            self.jump()

if __name__ == '__main__':
    g = Game("localhost:8083", 12345)
    g.run()
