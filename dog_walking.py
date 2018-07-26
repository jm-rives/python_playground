#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# Real Python Object Oriented programming tutorial
# https://realpython.com/python3-object-oriented-programming/

# Starter Code
# Would it be more logical to name this class 'Dogs' instead of Pets?
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    # Instance method
    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

# Parent class
class Dog:

    # Class attribute (changed to constant, science has not achieved trans-species tech, yet.)
    SPECIES = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def walk(self):
        return "{} is walking!".format(self.name)

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
# Create instances of dogs
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]
# Instanciate Pets class
my_pets = Pets(my_dogs)
