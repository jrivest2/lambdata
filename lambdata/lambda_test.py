"""Basic unit test for lambdata package"""

import unittest

from example_module import COLORS, FAVORITE_NUMBERS, increment
from oop_example import SocialMediaUser
from random import randint

class SocialMediaUserTests(unittest.TestCase):
    """Tests for the usage of Social Media Users in our Social Media Class"""
    def setUp(self):
        self.user1 = SocialMediaUser(name="Jimmy",location="France")
        self.user2 = SocialMediaUser(name="Craig",location="Kenya")
        self.user3 = SocialMediaUser(name="Nick",location="Nova Scotia")

    def test_name(self):
        """Testing the name attribute"""
        self.assertEqual(self.user1.name,"Jimmy")
        self.assertEqual(self.user2.name,"Craig")

    def test_location(self):
        """Testing the location attribute"""
        self.assertEqual(self.user1.location,"France")
        self.assertEqual(self.user2.location,"Kenya")

    def test_default_upvotes(self):
        """Testing default upvotes"""
        self.assertEqual(self.user3.upvotes, 0)

    def test_unpopular(self):
        """Testing is_popular method"""
        self.assertFalse(self.user3.is_popular())
        self.user3.recieve_upvotes(randint(101,1000))
        self.assertTrue(self.user3.is_popular())

class ExampleTests(unittest.TestCase):
    """Making sure examples work as expected"""
    def test_increment(self):
        """Testing that increment adds one to a number"""
        x0 = 0
        y0 = increment(x0) # y0 == 1
        self.assertEqual(y0,1)

        x1 = 100
        y1 = increment(x1) # y1 == 101
        self.assertEqual(y1,101)

        x2 = -1
        y2 = increment(x2) # x2 == 0
        self.assertEqual(y2,0)

        x3 = -1.5
        y3 = increment(x3) # x3 == -0.5
        self.assertEqual(y3,-0.5)
    


    def test_colors(self):
        """Testing the presence/absence of members in the colors list"""
        self.assertIn("crimson",COLORS)
        self.assertNotIn("brown",COLORS)
    
    def test_number_colors(self):
        """Testing htat we have the expected number of colors"""
        self.assertEqual(len(COLORS),5)


if __name__ == "__main__":
    unittest.main()