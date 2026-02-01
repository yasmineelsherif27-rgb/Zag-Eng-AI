import random
import os

class User():

    def __init__(self , name , password, email , allow_anonymous ):
        self.name = name

        id = random.randint(100 , 1000)
        self.id = id

        self.__password = password
        self.email = email
        self.allow_anonymous = allow_anonymous

        self.from_me_q = {}
        self.to_me_q = {}

    def __str__(self):
        return f"{self.id}|{self.name}|{self.email}|{self.allow_anonymous} "

    def to_line(self):
        return f"{self.id}|{self.name}|{self.email}|{self.allow_anonymous} "

#    def from_line(line):
#        for d in line :
#            line = line.split("|")

    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getEmail(self):
        return self.email
    
    def getAllowAnonymous(self):
        return self.allow_anonymous
    
    def setName(self , value):
        self.name = value

    def setEamil(self , value):
        self.email = value
    
    def setAllowAnonymous(self , value):
        self.allow_anonymous = value
    
    def check_password(self, password):
        return self.__password == password

    def set_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.__password = new_password
            return True
        return False


class Question():
    counter = 1
    def __init__(self  , from_user_id , to_user_id , Q_value):

        self.parent_id = Question.counter
        Question.counter +=1

        self.from_user_id = from_user_id
        self.to_user_id = to_user_id

        self.answered = False
        self.Q_value = Q_value

class Anonymous(Question):
    def __init__(self, from_user_id , to_user_id , Q_value):
        super().__init__(from_user_id, to_user_id , Q_value)
        self.from_user_id = "AQ"

class Thread(Question):
    def __init__(self, from_user_id, to_user_id, Q_value):
        super().__init__(from_user_id, to_user_id, Q_value)
        self.Q_id = Question.counter