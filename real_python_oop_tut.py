#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from "Object-Oriented Programming (OOP) in Python 3"
# https://realpython.com/python3-object-oriented-programming/
# # "The Oldest Dog" review exercise 1
class Dog:
    # Class Attribute
    animal_class = "mammal"

    # Initializer function with Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age



def get_biggest_number(list_of_dogs):
    """Accepts a list of Dog objects
    and returns the max age of dogs in the list. """
    dog_ages = []

    for dog in dogs:
        dog_ages.append(dog.age)
        oldest = max(dog_ages)

    print(f"The oldest dog is {oldest} years old.")


dana = Dog("Dana", 44)
balto = Dog("Balto", 50.0)
mandy = Dog("Mandy", 55)

dogs = [dana, balto, mandy]

get_biggest_number(dogs)
