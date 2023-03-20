#!/usr/bin/python3
"""Module to test the BaseModel class"""
from models.base_model import BaseModel
from time import sleep
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests the basemodel attributes and methods"""
    
    """
    def tearDown(self):
        A setup method that destroys instances
        print('teardown\n')
    """

    def test_id(self):
        """Tests for the value of id"""
        d1 = BaseModel()
        sleep(0.05)
        d2 = BaseModel()
        self.assertNotEqual(d1.id, d2.id)

    def test_created_at(self):
        """Tests for the value of created_at"""
        d1 = BaseModel()
        sleep(0.05)
        d2 = BaseModel()
        self.assertNotEqual(d1.created_at, d2.created_at)

    def test_save(self):
        """A test to check if the program saves"""
        d1 = BaseModel()
        sleep(0.05)
        d2 = BaseModel()
        d1.save()
        with open("file.json", "r") as f:
            self.assertIn(d1.id, f.read())

    def test_to_dict(self):
        """A test to check if the to_dict functions"""
        d1 = BaseModel()
        sleep(0.05)
        d2 = BaseModel()
        our_Dict = d1.to_dict()
        self.assertIn('__class__', our_Dict.keys())

    def test_str(self):
        """A test to checks for the string representation
            of an instance
        """
        d1 = BaseModel()
        sleep(0.05)
        d2 = BaseModel()
        our_Str = d1.__str__()
        self.assertIn("[BaseModel]", our_Str)


if __name__ == '__main__':
    unittest.main()
