import unittest
import maincode

class TestAlchemist(unittest.TestCase):
    def __init__(self):
        self.potions = []  # Initialize with empty lists for potions, herbs, and catalysts
        self.herbs = []
        self.catalysts = []
        

    def test_MixPotion(self):
        alchemist = Alchemist(self.potions, self.herbs, self.catalysts)

        alchemist.mixPotion("Super Attack")  # Test mixing super potion
        self.assertEqual(len(alchemist.getLaboratory().getPotions()), 1)  #Check if potion was added to laboratory
        
        
        alchemist.mixPotion("Extreme Defence")  # Test mixing extreme potion
        self.assertEqual(len(alchemist.getLaboratory().getPotions()), 2)  #Check if another potion was added to laboratory
        
        self.assertTrue("Super")
    unittest.main()

    def test_collectReagent(self):
            alchemist = Alchemist(self.potions, self.herbs, self.catalysts)

            herb = Herb("Irit", 1.2)
            alchemist.collectReagent(herb, 3)
            self.assertEqual(len(alchemist.getLaboratory().getHerbs()), 3)  # Check if herbs were added to the laboratory

            catalyst = Catalyst(5, "Eye of Newt", 3)
            alchemist.collectReagent(catalyst, 3)
            self.assertEqual(len(alchemist.getLaboratory().getCatalysts()), 3)  # Check if catalysts were added

    if __name__ == '__main__':
        unittest.main()

    def test_collectReagent():
        herb = Herb(name, potency)  
        name = 'Irit'      
        potency = 1.2      #potency
        amount  = 3

        catalyst = Catalyst(quality, name, catalyst)
        quality = 5
        name = 'Eye of Newt'
        amount = 3

