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
            alchemist = Alchemist()

            herb = Herb("Irit", 1.2)
            alchemist.collectReagent(herb, 3)
            self.assertEqual(len(alchemist.getLaboratory().getHerbs()), 3)  # Check if herbs were added to the laboratory

            catalyst = Catalyst(5, "Eye of Newt", 3)
            alchemist.collectReagent(catalyst, 3)
            self.assertEqual(len(alchemist.getLaboratory().getCatalysts()), 3)  # Check if catalysts were added

  

    def test_collectReagent(self):
        alchemist = Alchemist()
        name = 'Irit'      
        potency = 1.2      #potency
        herb = Herb(name, potency)  
        alchemist.collectReagent(herb, 4)  
        self.assertEqual(alchemist.getLaboratory().getHerbs()[-1], herb)
        
        quality = 5
        name = 'Eye of Newt'
        potency = 3
        catalyst = Catalyst(quality, name, potency)   #same as above
        
    def test_refineReagents(self):
        alchemist = Alchemist()
        irit = Herb ("Irit", 3.0)
        amount = 5
        alchemist.collectReagent(irit, amount)   #5 is amount
        alchemist.refineReagent()
        herbs = alchemist.getLaboratory().getHerbs()          #get list of herbs
        for herb in herbs:
            self.assertEqual(herb.getgrimy(), False)



if __name__ == '__main__':
    unittest.main()  


