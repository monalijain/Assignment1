__author__ = 'sony'

#Restaurant Problem

#Run this file

from Guest import *
from Restaurant import *

print("Enter restaurant size")
nSizeInput=int(input()) #Taking input from user for restaurant size
R = Restaurant(nSizeInput) #Making a restaurant with given restaurant size

print("Enter number of guests in a restaurant") #Asking user to enter number of guests in the restaurant
nNumberGuests=int(input())
#Creating a list of guests; asking user for name and hungervalue of guests
listGuest=[None]*nNumberGuests
for l in range(nNumberGuests):
    print("Enter name of guest",l+1)
    chGuestName=input()
    print("Enter hunger value of guest",l+1)
    nGuestHunger=int(input())
    listGuest[l] =Guest(chGuestName,nGuestHunger)

#Loop to seat the guests and serve them in the restaurant
bAvailable=True 
j=0
while(j<3):
    bAvailable= R.seat(listGuest[j])
    R.serve()
    if (bAvailable==True):
        j=j+1

