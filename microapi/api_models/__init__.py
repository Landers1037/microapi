# @Author: Landers1037
# @Github: github.com/landers1037
# @File: __init__.py.py
# @Date: 2020-05-31

class ApiModel:
    def __init__(self,path=''):
        self.__path = path

    def __getattr__(self, uri):
        return ApiModel('{}/{}'.format(self.__path,uri))

    def __repr__(self):
        return '/api{}'.format(self.__path)

class ApiTest:
    def __init__(self,path=''):
        self.__path = path

    def __getattr__(self, uri):
        return ApiTest('{}/{}'.format(self.__path,uri))

    def __repr__(self):
        return '/test/api{}'.format(self.__path)