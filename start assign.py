'''
File: filename.py
Description: A brief description of this Python module.
Author: Bhavya Gupta
StudentID: 110409283
EmailID: gupby005@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

def display_details():
    print("File     : gupby005_converter.py")
    print("Author   : Bhavya Gupta")
    print("Stud ID  : 110409283")
    print("Email ID : gupby005@mymail.unisa.edu.au")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    print("")
    print("")

display_details()

""" Imported the important method required for the abstract classes"""
from abc import ABC, abstractmethod


class Alchemist:
    def __init__(self, potions, herbs, catalysts): 
        """ Initially start at 0 and can range to 100  """
        self.__attack = 0
        self.__strength = 0
        self.__defense = 0
        self.__magic = 0
        self.__ranged = 0
        self.__necromancy = 0
        self.__laboratory = Laboratory(potions, herbs, catalysts) #composition     #private or public?   #None
        """ 'self.__recipes' stores a dictionary which represents the keys and values  """
        self.__recipes = {"Super Attack": ("Irit", "Eye of Newt"),
                          "Super Strength": ("Kwuarm", "Limpwurt Root"),
                          "Super Defence": ("Candantine", "White Berries"),
                          "Super Magic": ("Lantadyme", "Potato Cactus"),
                          "Super Ranging": ("Dwarf Weed", "Wine of Zamorak"),
                          "Super Necromancy": ("Arbuck", "Blood of Orcus"),
                          "Extreme Attack": ("Avantoe", "Blood of Orcus"),
                          "Extreme Strength": ("Dwarf Weed", "Super Strength"),
                          "Extreme Defence": ("Lantadyme", "Super Defence"),
                          "Extreme Magic": ("Ground Mud Rane", "Super Magic"),
                          "Extreme Ranging": ("Grenwall Spike", "Super Ranging"),
                          "Extreme Necromancy": ("Ground Miasma Rune", "Super Necromancy")
                        }

    def getLaboratory(self):
        """ Returns the laboratory associated with the alchemist class which can then be used for various operations """
        return self.__laboratory

    def getRecipes(self):
        """ Returns the recipes known by the alchemist """
        return self.__recipes

    def mixPotion(self, recipe):
        """ Initialises attribute ('recipe') of micPotion class. Then goes through keys of recipe. """
        self.__recipe = recipe
        if recipe in self.__recipe.keys():    
            """ Returns key names by getting the value from dictionary """
            primaryIngredient, secondaryIngredient = self.__recipe[recipe] 
            
            """ 
            Splits the recipe provided above to retrieve the 'type' and 'stat' 
            For example: Super Attack 
            .split() will assign 'Irit' as type and 'Eye of Newt' as stat
            
            """
            type, stat = recipe.split()

            """ '.mixPotion' then names all the ingredients from the recipe and mixes """
            self.__laboratory.mixPotion(recipe, type, stat, primaryIngredient, secondaryIngredient)   #name ingredients from recipe
     
    def drinkPotion(self, potion):  
        """ 
        Takes in two parameters of 'self' (instance of Alchemist class calling the method) and 
        'potion' (instance of Potion class representing the potion consumed)

        It then uses 'if' and elif' statements to determine the type of attribute the potion 
        will boost, by checking 'stat' using 'potion.getStat()'.

        Then updates attribute of alchemist by adding boost calculated by 'potion.calculateBoost()'.

        Once adjusted alchemist's attributes, string returns a message indicating which attribute has 
        has been boosted.

        """
        if potion.getStat() == "Attack":
            self.__attack += potion.calculateBoost()
        elif potion.getStat() == "Strength":
            self.__strength += potion.calculateBoost()
        elif potion.getStat() == "Defence":
            self.__defense += potion.calculateBoost()
        elif potion.getStat() == "Magic":
            self.__magic += potion.calculateBoost()
        elif potion.getStat() == "Ranging":
            self.__ranged += potion.calculateBoost()
        elif potion.getStat() == "Necromancy":
            self.__necromancy += potion.calculateBoost()
        return (f"I feel more {potion.getStat()}!")

    def collectReagent(self, reagent, amount):
        """ To collect a reagant and add it to the alchemist's laboratory using 'collect reagent """
        self.__laboratory.addReagent(reagent, amount)

    def refineReagents(self):
        """
        Checks if the alchemist has a laboratory via '.__laboratory' and if not None, then 
        continues with reagent refinement.

        '.refineCatalysts()' and '.refineHerbs()' refine catalsysts and herbs stored in the laboratory
        and if no laboratory found, then uses 'else' to return the message.
        
        """
        if self.__laboratory:
            self.__laboratory.refineCatalysts()
            self.__laboratory.cleanHerbs()
        
        
        else: 
            print("Alchemist has no laboratory to refine reagents")


class Laboratory:
    """Constructor method for the Laboratory class. """
    def __init__(self, potions, herbs, catalysts):
        """Takes three parameteres which are initialised. """
        self.__potions = potions  #coming in as a list
        self.__herbs = herbs
        self.__catalysts = catalysts
        self.__reagent = 0

    """
    Method used to mix a potiona and add it to the laboratory's list of potions. 
    Method checks if the potion is 'Super' or 'Extreme'.
    
    """
    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        """ 
        If potion is 'Super':
        Then a SuperPotion is created using the 'primaryIngredient' and 'secondaryIngredient'
        accordingly to the 'name' and 'stat'.

        New potion is then appended to the list of potions. 

        Otherwise if potion is 'Extreme':
        Then a ExtremePotion is created using the 'primaryIngredient' and 'secondaryIngredient'
        accordingly to the 'name' and 'stat'.

        New potion is then appended to the list of potions. 
        """
        if type == "Super":
            potion = SuperPotion(primaryIngredient, secondaryIngredient, name, stat)  #mixing ingredients to create super potion ##herb, catalyst
            self.__potions.append(potion)

        elif type == "Extreme":
            potion = ExtremePotion(primaryIngredient, secondaryIngredient, name, stat)    ##catalyst, other potion
            self.__potions.append(potion) #add potion to potion lift

    def addReagent(self, reagent, amount):
        """ Checks if reagent has Herb or Catalyst via 'if'/'else'. Then goes through a loop for herbs being added. """
        if isinstance(reagent, Herb):
            for i in range(amount):                
                self.__herbs.append(reagent)
                print(f"")

        
        elif isinstance(reagent, Catalyst):
            for i in range(amount):        #loop for catalysts being added amount num of times
                self.__catalysts.append(reagent)
                print(f"The ")  
    
        """ Displays the total number of reagents by adding herbs and catalysts together. """
        print(f"Total number of reagents {len(self.__herbs)} + {len(self.__catalysts)}")

        

class Potion(ABC):
    """ 
    Constructor method used to initialise instances of the Potion class 
    The class serves as a blueprint for creating specific types of potions
    
    """
    def __init__(self, name, stat):
        self.__name = name
        self.__stat = stat
        self.__boost = 0
    
    """ Calculates the boost value that can get changed later in child classes."""
    @abstractmethod
    def calculateBoost():
        pass  #return round(self.boost, 2)

    def getName(self):  
        """ Returns name of a potion. """
        return self.__name

    def getStat(self):
        """ Returns the statistic associated with the potion. """
        return self.__stat

    def getBoost(self): 
        """ Returns the boost value of the potion. """
        return self.__boost

    def setBoost(self, boost):
        """ Allows settign the boost value of potion. """
        self.__boost = boost


class SuperPotion(Potion):
    """ Initialise the attributes and refers to superclass using 'super'. """
    def __init__(self, herb, catalyst, name, stat):
        super().__init(name, stat)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        """ Calulates the boost of super potion using herb and catlayst. """
        value = self.__herb.getPotency() + (self.__catalyst.getQuality() * self.__catalyst.getPotency()) * 1.5
        return round(value, 2)   
    
    def getHerb(self):
        """ Returns the herb associated with SuperPotion. """
        return self.__herb   
    
    def getCatalyst(self): 
        """ Returns the herb associated with SuperPotion. """
        return self.__catalyst
    

class ExtremePotion(Potion):
    """ Initialises the attributes and refers to superclass using 'super'. """
    def __init__(self, reagent, potion, name, stat):
        super().__init(name, stat)
        self.__reagent = reagent #catalyst
        self.__potion = potion  

    def calculateBoost(self):
        """ Calulates the boost of extreme potion using reagent and super potion. """
        value = self.__reagent.getPotency() + (self.__stat.getQuality() * self.__stat.getPotency()) * 3.0
        return round(value, 2) 

    def getReagent(self):
        """ Returns reagent associated with ExtremePotion. """
        return self.__reagent

    def getPotion(self):
        """ Returns potions associated with ExtremePotion. """
        return self.__potion



class Reagent(ABC):
    """ Initialises the attributes and refers to abstract class using 'ABC'. """
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    """ Refines the reagent in where two methods exist depending on the child class. """
    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        """ Returns the name of the reagent. """
        return self.__name

    def getPotency(self): 
        """ Returns the potency of the reagent. """
        return self.__potency

    def setPotency(self, potency):    
        """ Setter method is used to update the potency of the reagent. """        
        self.__potency = potency


class Herb(Reagent):
    """ Initialises the attributes and refers to superclass using 'super'. """
    def __init__(self, name, potency):
        super().__init(name, potency)
        self.__grimy = True

    def refine(self):
        """ Calls the herb class method where refining leads to a herb that is not grimy. """
        self.setGrimy(False) #herb class method call. refining leads to a herb that is not grimy

        self.setPotency(self.getPotency * 2.5)
        print(f"Cleaned. Potency increased to {self.getPotency()}") 

    def getGrimy(self):
        """ Getter method used to retrieve the 'grimy' attribute value. """
        return self.__grimy

    def setGrimy(self, grimy):
        """ Setter method used to update the 'grimy' attribute of the herb. """
        self.__grimy = grimy 

   


class Catalyst(Reagent):
    """ Initialises the attributes and refers to superclass using 'super'. """
    def __init__(self, quality, name, potency):
        super().__init(name, potency)
        self.__quality = quality

    """ 
    The method of refining the catalyst depends on its' exisitng quality.

    Checks if quality is less than 8.9, then increase it by 1.1. 
    Once refining is complete, message is printed indicating the new quality value. 

    Else:
    If the quality is 8.9 or greater, then catalyst cannot be refined any further. 
    So set quality to 10 and print message stating no more refinement. 
     
    """
    def refine(self):
        if self.quality < 8.9:
            self.quality += 1.1
            print(f"Quality is {self.quality}")

        else:
            self.quality = 10 
            print(f"The quality is {self.quality}. Catalyst cannot be refined any further")

    def getQuality(self):
        """ Returns the quality of the catalyst. """
        return self.quality

    

