__author__ = 'sony'

#Guest Class which initialize the guest object with name and hungervalue
class Guest(object):

    def __init__(self,chName,nHungerValue):
        self.chName=chName
        self.nHungerValue=nHungerValue

#Eat function which reduces the hunger value by 1 and if hunger <=0, the guest burps
    def eat(self):
        self.nHungerValue=self.nHungerValue-1
        if self.nHungerValue<1:
            print(self.chName, ": Burp!")
            print(self.nHungerValue)

        return self.nHungerValue



