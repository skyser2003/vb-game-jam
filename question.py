class Question:
    __answer = 0

    def isTrue(self):
        return self.__answer
    
class TrueFalseQuestion(Question):
    __answer = True

    def isTrue(self):
        return self.__answer

class LoveQuestion(TrueFalseQuestion):
    __LoverDir = ""
    __LoveeDir = ""

    def __init__(self,_LoverDir,_LoveeDir,_answer):
        self.__LoverDir = _LoverDir
        self.__LoveeDir = _LoveeDir
        self.__answer = _answer
    def getLoverDir(self):
        return self.__LoverDir
    def getLoveeDir(self):
        return self.__LoveeDir
