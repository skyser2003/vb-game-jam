class Question:
    answer = None

    def isTrue(self):
        return self.answer
    
class TrueFalseQuestion(Question):
    answer = True

    def isTrue(self):
        return self.answer

class LoveQuestion(TrueFalseQuestion):
    LoverDir = ""
    LoveeDir = ""

    def __init__(self,LoverDir,LoveeDir,answer):
        self.LoverDir = LoverDir
        self.LoveeDir = LoveeDir
        self.answer = answer
    def getLoverDir(self):
        return self.LoverDir
    def getLoveeDir(self):
        return self.LoveeDir
