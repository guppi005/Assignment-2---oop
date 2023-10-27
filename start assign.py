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
        self.__magic = magic    #0
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = Laboratory(potions, herbs, catalysts) #composition     #private or public?   #None
        self.__recipes = recipes #{}

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe):
        self.__recipe = recipe
        self.__laboratory.mixPotion(potionName, primaryIngredient, secondaryIngredient)
    
    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        if self.__laboratory:
            self.__laboratory.addReagent(reagent, amount)

        else:
            print("Alchemist has no laboratory to collect reagents")

    def refineReagents(self):
        if self.__laboratory:
            self.__laboratory.refineCatalysts()
            self.__laboratory.cleanHerbs()
        
        else: 
            print("Alchemist has no laboratory to refine reagents")


class Laboratory:
    def __init__(self, potions, herbs, catalysts):
        self.__potions = potions  #coming in as a list
        self.__herbs = herbs
        self.__catalysts = catalysts
        self.__reagent = 0

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        if type == "Super":
            potion = SuperPotion(primaryIngredient, secondaryIngredient, name, stat)  #mixing ingredients to create super potion ##herb, catalyst
            self.__potions.append(potion)

        elif type == "Extreme":
            potion = ExtremePotion(primaryIngredient, secondaryIngredient, name, stat)    ##catalyst, other potion
            self.__potions.append(potion) #add potion to potion lift

    def addReagent(self, reagent, amount):
        if isinstance(reagent, Herb):
            for i in range(amount):                #loop for herbs being added amount num of times
                self.__herbs.append(reagent)
                print(f"")

        elif isinstance(reagent, Catalyst):
            for i in range(amount):        #loop for catalysts being added amount num of times
                self.__catalysts.append(reagent)
                print(f"")  ###########
        print(f"Total number of reagents {len(self.__herbs)} + {len(self.__catalysts)}")

    def grabReagent(self, name):
        pass

    def cleanHerbs(self):
        pass

    def refineCatalysts(self):
        pass
        

class Potion(ABC):
    def __init__(self, name, stat):
        self.__name = name
        self.__stat = stat
        self.__boost = 0
    
    @abstractmethod
    def calculatedBoost():
        pass  #return round(self.boost, 2)

    def getName(self):  
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self): 
        return self.__boost

    def setBoost(self, boost):
        self.__boost = boost


class SuperPotion(Potion):
    def __init__(self, herb, catalyst, name, stat):
        super().__init(name, stat)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        value = self.__herb.getPotency() + (self.__catalyst.getQuality() * self.__catalyst.getPotency()) * 1.5
        return round(value, 2)   #calculate boost
    
    def getHerb(self):
        return self.__herb   #same catalyst
    
    def getCatalyst(self): 
        return self.__catalyst
    

class ExtremePotion(Potion):
    def __init__(self, reagent, potion, name, stat):
        super().__init(name, stat)
        self.__reagent = reagent #catalyst
        self.__potion = potion  

    def calculateBoost(self):
        return self.__boost

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion



class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self): 
        return self.__potency

    def setPotency(self, boost):            ######boost or potency???
        self.__boost = boost


class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init(name, potency)
        self.__grimy = True

    def refine(self):
        self.setGrimy(False) #herb class method call. refining leads to a herb that is not grimy

        self.setPotency(self.getPotency * 2.5)
        print(f"Cleaned. Potency increased to {self.getPotency()}") #

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy):
        self.__grimy = grimy

   


class Catalyst(Reagent):
    def __init__(self, quality, name, potency):
        super().__init(name, potency)
        self.__quality = quality

    def refine(self):
        if self.quality < 8.9:
            self.quality += 1.1
            print(f"Quality is {self.quality}")

        else:
            self.quality = 10 
            print(f"The quality is {self.quality}. Catalyst cannot be refined any further")

    def getQuality(self):
        return self.quality

    






