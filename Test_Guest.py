__author__='sony'

#Test Cases for guest class; Run this file to run the test cases

import unittest
from Guest import *

class GuestAttributeTestCase(unittest.TestCase):
    def RunTest(self):
        guest=Guest('Monali',3)
        assert guest.chName=='Monali','incorrect name of guest'
        assert guest.nHungerValue==3,'incorrect hunger value'
        print("Test of guest attributes is successful")

class GuestEatTestCase(unittest.TestCase):
    def RunTest(self):
        guest=Guest('Monali',1)
        guest.eat()
        assert guest.nHungerValue==0,'Eating function is not working'
        print("Test of Eat function in Guest class is successful")

TestCase=GuestAttributeTestCase()
TestCase.RunTest()

TestCase=GuestEatTestCase()
TestCase.RunTest()
        


