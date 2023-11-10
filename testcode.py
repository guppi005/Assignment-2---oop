import unittest
import maincode

class TestAlchemist(unittest.TestCase):
    """Initialize with empty lists for potions, herbs, and catalysts"""
    def __init__(self):
        self.potions = []  
        self.herbs = []
        self.catalysts = []
        

    def test_mixPotion(self):
        """ Create instance of Alchemist class to then test its' methods. """
        alchemist = Alchemist(self.potions, self.herbs, self.catalysts)

        """ Test mixing extreme potion. """
        alchemist.mixPotion("Super Attack")  

        """ Check if potion was added to laboratory. """
        self.assertEqual(len(alchemist.getLaboratory().getPotions()), 1)  
        
        """ Test mixing extreme potion"""
        alchemist.mixPotion("Extreme Defence") 

        """ Check if another potion was added to laboratory. """
        self.assertEqual(len(alchemist.getLaboratory().getPotions()), 2)  
        
        self.assertTrue("Super")  ##what to do with this????????
   

    def test_collectReagent(self):
        """ Create instance of Alchemist class to then test its' methods. """
        alchemist = Alchemist(self.potions, self.herbs, self.catalysts)

        name = 'Irit'
        potency = 1.2
        herb = Herb(name, potency)
        alchemist.collectReagent(herb, 3)

        """ Check if herbs were added to the laboratory. """
        self.assertEqual(len(alchemist.getLaboratory().getHerbs()), 3)  

        quality = 5
        name = 'Eye of Newt'
        potency = 3
        catalyst = Catalyst(name, quality, potency)
        alchemist.collectReagent(catalyst, 3)
        """ Check if herbs were added to the laboratory. """
        self.assertEqual(len(alchemist.getLaboratory().getCatalysts()), 3) 

    def test_refineReagents(self):
        #test method 1
        """ Create instance of Alchemist class to then test its' methods. """
        alchemist = Alchemist(self.potions, self.herbs, self.catalysts)
        """Create the instance of 'Herb' class and 'Catalyst' class witht the given name and potency. """
        herb = Herb ("Irit", 3.0) 
        catalyst = Catalyst(7.8, "Eye Of Newt", 3)
        """ Calls the 'collectreagent' method and add the herb/catalyst to the alchemist laboratory. """
        alchemist.collectReagent(herb, 1)
        alchemist.collectReagent(catalyst, 1)


        alchemist.refineReagents()
        """ According to the formula of Herb.refine()"""
        self.assertEqual(herb.getPotency(), 1.2 * 2.5) 
        self.assertEqual(catalyst.getQuality(), 8.9)

        #test method 2... done with you
        amount = 5
        alchemist.collectReagent('Irit', amount)  
        alchemist.refineReagent()
        """ Get list of herbs. """
        herbs = alchemist.getLaboratory().getHerbs()        
        for herb in herbs:
            self.assertEqual(herb.getgrimy(), False)



class TestLaboratory(unittest.TestCase):
    """ Initialize with empty lists for potions, herbs, and catalysts. """
    def __init__(self):
        self.potions = []  
        self.herbs = []
        self.catalysts = []
        
    def test_mixPotion(self):
        """ Create instance of Laboratory class to then test its' methods. """
        laboratory = Laboratory(self.potions, self.herbs, self.catalysts)

        laboratory.mixPotion("Super Attack", "Super", "Attack", "Irit", "Eye of Newt")
        
        self.assertEqual(len(self.laboratory.getPotions()), 1)
        self.assertEqual(self.laboratory.getPotions()[0].getName(), "Super Attack")


    def test_addReagent(self):
        """ Create instance of Laboratory class to then test its' methods. """
        laboratory = Laboratory(self.potions, self.herbs, self.catalysts)
       
        herb = Herb("Irit", 1.2)
        catalyst = Catalyst(5, "Eye of Newt", 3)

        laboratory.addReagent(herb, 3)
        self.assertEqual(len(self.laboratory.getHerbs()), 3)

        laboratory.addReagent(catalyst, 2)
        self.assertEqual(len(self.laboratory.getCatalysts()), 2)

    
    def test_refineReagents(self):
        """ Create instance of Laboratory class to then test its' methods. """
        laboratory = Laboratory(self.potions, self.herbs, self.catalysts)

        herb = Herb("Irit", 1.2)
        catalyst = Catalyst(5, "Eye of Newt", 3)

        laboratory.addReagent(herb, 1)
        laboratory.addReagent(catalyst, 1)

        laboratory.refine()
        self.assertEqual(herb.getPotency(), 1.2 * 2.5)
        self.assertEqual(catalyst.getQuality(), 8.9)



    class TestPotion(unittest.TestCase):
        def __init__(self):
            pass   # put for initialiser for abstract class

        def test_set_boost(self):
            """ Create a SuperPotion instance. """
            superPotion = SuperPotion("Irit", "Eye of Newt", "Super Attack", "Attack") 

            superPotion.setBoost(3)  
            self.assertEqual(superPotion.getBoost(), 3)
        

    class TestSuperPotion(unittest.TestCase):
        def test_calculateBoost(self):
            superPotion = SuperPotion(herb, catalyst, "Super Attack", "Attack")
            
            herb = Herb("Irit", 1.2)
            catalyst = Catalyst(7.8, "Eye of Newt", 3)

            self.assertEqual(superPotion.getHerb(), herb)
            self.assertEqual(superPotion.getCatalyst(), catalyst)
            self.assertEqual(superPotion.getName(), "Super Attack")
            self.assertEqual(superPotion.getStat(), "Attack")


    class TestExtremePotion(unittest.TestCase):
        def test_calculateBoost(self):
            extremePotion = ExtremePotion(reagent, super_potion, "Extreme Strength", "Strength")

            herb = Herb("Kwuarm", 1.5)
            catalyst = Catalyst(6.5, "Limpwurt Root", 2)
            super_potion = SuperPotion(herb, catalyst, "Super Strength", "Strength")
            reagent = Catalyst(7.8, "Eye of Newt", 3)
            """ Calculate the expected boost value. """
            expectedBoost = reagent.getPotency() + (super_potion.getCatalyst().getQuality() * super_potion.getCatalyst().getPotency()) * 3.0
            expectedBoost = round(expectedBoost, 2)
            """Check if the calculated boost matches the expected boost. """
            self.assertEqual(extremePotion.calculateBoost(), expectedBoost)


    class TestReagent(unittest.TestCase):
        def test_setPotency(self):
            reagent = Reagent(name, potency)
            
            name = "herb"
            potency = 2.5
            """ Set a new potency value. """
            newPotency = 3.0
            reagent.setPotency(newPotency)
            """Check if the new potency is set correctly. """
            self.assertEqual(reagent.getPotency(), newPotency)


    class TestHerb(unittest.TestCase):
        def test_refine(self):
            herb = Herb(name, potency)
            
            name = "Irit"
            potency = 1.2
            """Set the herb to be grimy. """
            herb.setGrimy(True)
            """ Refine the herb. """
            herb.refine()
            """ Check if the herb is no longer grimy. """
            self.assertFalse(herb.getGrimy())
            """Check if the potency is increased to the expected value. """
            expectedPotency = 1.2 * 2.5
            self.assertEqual(herb.getPotency(), expectedPotency)


    class TestCatalyst(unittest.TestCase):
        """This is to test when quality is < 10. """
        def test_refine(self):
            catalyst = Catalyst(quality, name, potency)

            quality = 7.8
            name = 'Eye of Newt'
            potency = 3
            """ Call the refine method to refine the catalyst. """
            catalyst.refine()
            """ Check if the quality is increased by 1.1 as expected. """
            expected_quality = 7.8 + 1.1
            self.assertEqual(catalyst.getQuality(), expected_quality)
        
        
        def test_refine(self):
            catalyst = Catalyst(quality, name, potency)

            """This is to test when quality is = 10 (maximum). """
            quality = 10
            name = 'Eye of Newt'
            potency = 3
            """ Call the refine method. """
            catalyst.refine()
            """ Check if the quality remains at the maximum (10) and cannot be refined further. """
            self.assertEqual(catalyst.getQuality(), 10)
            """ Check if the printed message indicates that the catalyst cannot be refined further. """
            self.assertEqual(catalyst.refine(), "The quality is 10. Catalyst cannot be refined any further. ")

        

if __name__ == '__main__':
    unittest.main()  


