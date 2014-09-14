__author__ = 'sony'

#Test Cases for Restaurant Class; Run this file to test all the test cases
import unittest
from Restaurant import *

class RestaurantAttributeTestCase(unittest.TestCase):
    def RunTest(self):
        TestR=Restaurant(2)
        assert TestR.nSize==2,'Incorrect size of the restaurant'
        assert TestR.listTable==[None]*2
        print("Test of Restaurant Attributes is successful\n")

class RestaurantSeatFunctionTestCase(unittest.TestCase):
    def RunTest(self):
        TestR=Restaurant(2)
        guest=Guest('Mary',3)
        assert TestR.seat(guest)==True,'Incorrect seating function'
        guest1=Guest('John',2)
        assert TestR.seat(guest1)==True,'Incorrect seating function'
        guest2=Guest('Alice',1)
        assert TestR.seat(guest2)==False,'Incorrect seating function'
        print("Test of seating function in restaurant is successful\n")

class RestaurantServeFunctionTestCase(unittest.TestCase):
    def RunTest(self):
        TestR=Restaurant(2)
        guest=Guest('Mary',3)
        TestR.seat(guest)
        TestR.serve()
        assert guest.nHungerValue==2,'incorrect serving function'
        guest1=Guest('John',2)
        TestR.seat(guest1)
        TestR.serve()
        assert guest.nHungerValue==1,'incorrect serving function'
        TestR.serve()
        assert guest.nHungerValue==0,'incorrect serving function'
        guest2=Guest('Alice',1)
        TestR.seat(guest2)
        TestR.serve()
        assert guest2.nHungerValue==0,'incorrect serving function'
        print("Test of serving function is successful")
        
TestCase=RestaurantAttributeTestCase()
TestCase.RunTest()

TestCase=RestaurantSeatFunctionTestCase()
TestCase.RunTest()
        
TestCase=RestaurantServeFunctionTestCase()
TestCase.RunTest()
