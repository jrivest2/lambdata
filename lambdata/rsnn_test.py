"""Unit test for lambdata package - specifically the rsnn module"""

import unittest

import pandas as pd
import numpy as np

from rsnn import *

class DFTests(unittest.TestCase):
    """Testing that the DF class works as expected"""
    
    def setUp(self):
        self.df = pd.DataFrame({"A":[np.NaN,1,2],"B":[3,4,5],"C":[6,np.NaN,8]})
        self.df = DF(data=self.df)
        self.dfr = self.df.randomShuffle()

    def test_numNull(self):
        """Testing that the numNull method reports the correct number of null values in the dataframe
        """
        self.assertEqual(self.df.numNull(),2)


    def test_randomShuffle(self):
        """Testing that randomShuffle effectively randomizes order of \n observations and correctly resets the index
        """

        """Check that all the same data is there by using to total sum of all numbers in each dataframe"""
        self.assertEqual(self.df.sum().sum(),self.dfr.sum().sum())

        """
        Check that the first index in one of the columns is not the
         same as it was prior to the shuffle
        """
        self.assertFalse(self.df['B'][0]==self.dfr['B'][0])




if __name__ == "__main__":
    unittest.main()