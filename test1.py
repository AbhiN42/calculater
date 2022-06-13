import unittest
import Class_base_calculater
class Test_Class_base_calculater(unittest.TestCase):
    def test__init__(self,assertEquals):
        self.assertEquals = assertEquals
    def test__add(self):
        Ans = Class_base_calculater.add(1,1)
        expected  = 2
        self.assertEquals(Ans, expected)     
    def test__sub(self):
        Ans = Class_base_calculater.sub(1,1)
        expected  = 0
        self.assertEquals(Ans, expected)    
    def test__mul(self):
        Ans = Class_base_calculater.mul(1,1)
        expected  = 1
        self.assertEquals(Ans, expected)
    def test__div(self):
        Ans = Class_base_calculater.div(1,1)
        expected  = 1
        self.assertEquals(Ans, expected)    