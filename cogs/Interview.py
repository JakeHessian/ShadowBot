import discord
from discord.ext import commands
"""
member - Member discord object
        the interviewy
responses [] - list of responses strings
questions [] - list of questions

"""


class Interview:
    def __init__(self, questions, member):
        self.memberObject = member
        self.memberName = member.name
        self.responses = []
        self.questions = questions

    def getMember(self):
        return self.memberObject

    def getNextQuestion(self):
        question = self.questions[0]
        if (len(self.questions) == 1):
            self.questions = []
        else:
            self.questions = self.questions[1:]
        return question

    def isEmpty(self):
        return len(self.questions) == 0


def loadQuestions():
    questions = []
    print("loading apllication questions...")
    questionFile = open("AppQuestions.txt", 'r')
    for item in questionFile:
        questions.append(item)
    questionFile.close()
    print("done")
    return questions
