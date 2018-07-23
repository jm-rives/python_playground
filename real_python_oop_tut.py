#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from "Object-Oriented Programming (OOP) in Python 3"
# https://realpython.com/python3-object-oriented-programming/
# # "The Oldest Dog" review exercise 1
class Dog:

    animal_class = "mammal"

    # Initializer function with Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

dana = Dog("Dana", 44)
balto = Dog("Balto," 50)
mandy = Dog("Mandy", 55)
