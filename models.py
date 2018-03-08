# -*-coding:utf-8-*-
from __future__ import unicode_literals

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
