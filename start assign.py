#
#File: gupby005_converter.py
#Author: Bhavya Gupta
#Email Id: gupby005@mymail.unisa.edu.au
#Description: Assignment 2 - 
#This is my own work as defined by the University's 
#Academic Misconduct policy
#


def display_details():
    print("File     : gupby005_converter.py")
    print("Author   : Bhavya Gupta")
    print("Stud ID  : 110409283")
    print("Email ID : gupby005@mymail.unisa.edu.au")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    print("")
    print("")

display_details()



from abc import ABC, abstractmethod
class Alchemist:
    def __init__(self, attack, potions):
        self.attack = attack
        self.recipes = {}
        self.laboratory = Laboratory(potions, herbs, catalysts) #composition

    def getLaboratory(self):
        pass

    def mixPotion(self, recipe):
        pass


class Laboratory:
    def __init__(self, potions):
        self.__potions = potions   #coming in as a list

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass
        

class Potion(ABC):
    
    @abstractmethod
    def calculatedBoost():
        pass

class SuperPotion(Potion):
    def __init__(self, herb):
        self.herb = herb

    def getHerb(self):
        return self.herb   #same catalyst
    

class Reagent:
    def __init__(self):
        pass


class Herb(Reagent):
    def __init__(self):
        self.__grimy = True




