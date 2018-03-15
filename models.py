# -*-coding:utf-8-*-
from __future__ import unicode_literals

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
    def set(self, data):
        self.energy = data["energy"]
        self.magic = data["magic"]
        self.score = data["score"]
        self.print_all()

    def print_all(self):
        print ">>>>>Energy:" + str(self.energy) + " Magic:" + str(self.magic) + " Score:" + str(self.score)

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
    def set(self, data):
        self.pool = data["pool"]
        self.board = data["board"]


'''
raise exception when code is nto 200
'''
class HTTPCodeError(Exception):
    pass

'''
raise exeption when return json code error
'''
class GameCodeError(Exception):
    pass

'''
raise
'''
class InvalidInputError(Exception):
    pass
