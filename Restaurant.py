__author__ = 'sony'

#Restaurant Class

from Guest import *

class Restaurant():

    def __init__(self,nSize): #Constructor initializes the restaurant with given input size and creates empty list of tables
        self.nSize=nSize
        self.listTable=[None] * self.nSize

    def seat(self,Guest): #Seating method assign an empty table to the guest; if no empty table, the guest waits
        nSeat=1
        for i in range(0,self.nSize):
            if self.listTable[i] == None :
                self.listTable[i]= Guest
                print("Seating guest",self.listTable[i].chName,"at table",i)
                nSeat=0
                return True

        if nSeat==1:
            print("No free table")
            return False

        print(self.listTable[0:self.nSize])

    def serve(self): #Serving method serves the seated guests 1 portion at a time until their hunger reduces to 0, and then removes the guest from the table
        nServe=1
        for i in range(0,self.nSize):
            if self.listTable[i] != None:
                if self.listTable[i].nHungerValue> 0:
                    nServe=0
                    print("Serving guest",self.listTable[i].chName)
                    if(self.listTable[i].eat()<=0):
                        self.listTable[i]=None
                    break
                else:
                    self.listTable[i]=None

        if nServe==1:
            print("No guest to serve")

