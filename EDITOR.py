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
        self.__laboratory = Laboratory(potions, herbs, catalysts) #composition     #private or public?
        self.__recipes = {"Super Attack": ("Irit", "Eye of Newt"),
            "Super Strength": ("Kwuarm", "Limpwurt Root"),
            "Super Defence": ("Cadantine", "White Berries"),
            "Super Magic": ("Lantadyme", "Potato Cactus"),
            "Super Ranging": ("Dwarf Weed", "Wine of Zamorak"),
            "Super Necromancy": ("Arbuck", "Blood of Orcus"),
            "Extreme Attack": ("Avantoe", "Super Attack"),
            "Extreme Strength": ("Dwarf Weed", "Super Strength"),
            "Extreme Defence": ("Lantadyme", "Super Defence"),
            "Extreme Magic": ("Ground Mud Rune", "Super Magic"),
            "Extreme Ranging": ("Grenwall Spike", "Super Ranging"),
            "Extreme Necromancy": ("Ground Miasma Rune", "Super Necromancy")}

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe):
        pass
    
    def drinkPotion(self, potion):
        
        if potion.getStat() == "Attack":
            self.attack += potion.calculateBoost()
        elif potion.getStat() == "Strength":
            self.strength += potion.calculateBoost()
        elif potion.getStat() == "Defence":
            self.defense += potion.calculateBoost()
        elif potion.getStat() == "Magic":
            self.magic += potion.calculateBoost()
        elif potion.getStat() == "Ranging":
            self.ranged += potion.calculateBoost()
        elif potion.getStat() == "Necromancy":
            self.necromancy += potion.calculateBoost()
        return f"*gulp...gulp...gulp. I feel more {potion.getStat()}. My {potion.getStat()} increased to {self.__getattribute__(potion.getStat())}"


    def collectReagent(self, reagent, amount):
        pass

    def refineReagents(self):
        pass


class Laboratory:
    def __init__(self, potions, herbs, catalysts):
        self.__potions = potions  #coming in as a list
        self.__herbs = herbs
        self.__catalysts = catalysts

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

    def setBoost(self, boost):
        self.__boost = boost


class SuperPotion(Potion):
    def __init__(self, herb, catalyst, name, stat, boost):
        super().__init(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def getHerb(self):
        pass
    
    def getHerb(self):
        return self.herb   #same catalyst
    
    def getCatalyst(self):
        pass
    

class ExtremePotion(Potion):
    def __init__(self, reagent, potion, name, stat, boost);
        super().__init(name, stat, boost)
    def calculateBoost(self):
        pass

    def getReagent(self):
        pass

    def getPotion(self):
        pass



class Reagent(ABC):
    def __init__(self, name potency):
        super().__init(name, potency)
        self.__name = name

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self):
        pass

    def setPotency(self, boost):
        self.__boost = boost


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
    def __init__(self, quality, name, potency):
        super().__init(name, potency)



    def refine(self):
        pass

    def getQuality(self):
        pass






