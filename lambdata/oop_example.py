"""OOP examples for Module 2"""
import pandas as pd
import numpy as np

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1]

    



class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        """
        Constructor for complex numbers.
        Complex numbers have a real part and an imaginary part.
        """
        self.r = realpart
        self.i = imagpart
    

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({},{})'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)
    
    def recieve_upvotes(self, num_upvotes=1):
        self.upvotes += num_upvotes

    def is_popular(self):
        return self.upvotes > 100
    
class Animal:
    """General Representation of Animals"""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight= float(weight)
        self.diet_type = diet_type
    
    def run(self):
        return "Vroom, Vroom, I go quick!"

    def eat(self, food):
        return "Huge fan of that " + str(food)
    
class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps):
        super().__init__(name,weight,diet_type)
        self.num_naps = int(num_naps)

    def say_something(self):
        return "Hi, I'm a sloth!"

    def run(self):
        return "I am a slow sloth guy."

if __name__ == '__main__':

    num1 = Complex(3,5)
    num2 = Complex(4,2)

    num1.add(num2)
    print(num1.r, num1.i)

    user1 = SocialMediaUser('Justin','Provo')
    user2 = SocialMediaUser('Nick','Logan',200)
    user3 = SocialMediaUser('Carl','Costa Rica',1000000000)
    user4 = SocialMediaUser('George Washington','Djibouti',2)
    print("name: {}, is popular: {}, num upvotes: {}".format(user4.name, user4.is_popular(), user4.upvotes))
    print("name: {}, is popular: {}, num upvotes: {}".format(user3.name, user3.is_popular(), user3.upvotes))
