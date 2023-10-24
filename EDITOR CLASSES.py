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
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory, recipes, potions, herbs, catalysts):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__recipes = {}
        self.laboratory = Laboratory(potions, herbs, catalysts) #composition     #private or public?

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe):
        pass
    
    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagents(self):
        pass


class Laboratory:
    def __init__(self, potions, herbs, catalysts):
        self.__potions = []   #coming in as a list
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagent(self, reagent, amount):
        pass

    def grabReagent(self, name):
        pass

    def cleanHerbs(self):
        pass

    def refineCatalysts(self):
        pass
        

class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
    
    @abstractmethod
    def calculatedBoost():
        pass

    def getName(self):
        pass

    def getStat(self):
        pass

    def getBoost(self):
        pass

    def setBoost(self):
        self.__boost = boost


class SuperPotion(Potion):
    def __init__(self, herb):
        super().__init__()
        self.__herb = herb
        self.__catalyst = catalyst

    def getHerb(self):
        pass
    
    def getHerb(self):
        return self.herb   #same catalyst
    
    def getCatalyst(self):
        pass
    

class ExtremePotion(Potion):
    def calculateBoost(self):
        pass

    def getReagent(self):
        pass

    def getPotion(self):
        pass



class Reagent:
    def __init__(self, name, potency):
        self.__name = []

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self):
        pass

    def setPotency(self, boost):
        pass


class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init(name, potency)
        self.__grimy = True

    def refine(self):
        pass

    def getGrimy(self):
        pass

    def setGrimy(self, grimy):
        pass

class Catalyst(Reagent):
    def __init__(self, quality):
        pass

    def refine(self):
        pass

    def getQuality(self):
        pass






