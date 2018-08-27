'''
MIT License

Copyright (c) 2018 Diego Duque

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

class PoolManager:
    __instance = None
    __res = list()
    __poolSize=0  

    def __init__(self):
        if PoolManager.__instance != None:
            raise NotImplemented("The class can not be initialized because it is of type of singleton type.")

    def setPoolSize(self, poolSize):
        self.__poolSize = poolSize
    
    @staticmethod
    def getInstance():
        if PoolManager.__instance == None:
            PoolManager.__instance = PoolManager()
        return PoolManager.__instance

    def setResourceHandler(self, handler):
        setattr(self,"getObjectResource",handler)

    def getResource(self):
        if(self.__poolSize==0):
            raise Exception('The poolSize is not specified')
        
        if not hasattr(self, 'getObjectResource'):
            raise Exception('Resource management has not been specified (getObjectResource)')

        if len(self.__res) > 0:          
            return self.__res.pop(0)
        else:
            if len(self.__res) < self.__poolSize:
                return self.getObjectResource()
            else:
                raise Exception('The maximum size of the pool has been exceeded')

    def release(self, obj):
        self.__res.append(obj)