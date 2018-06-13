import  unittest
import VendingMachine

class TestUnittest(unittest.TestCase):
    def TestProcessing(self):
        self.assertEquals(VendingMachine.Processing("Coke"), "Coke")
        self.assertEquals(VendingMachine.Processing("Pepsi"), "Pepsi")
        self.assertEquals(VendingMachine.Processing("7up"), "Redbull")
    def TestRepeation(self):
        self.assertEquals(VendingMachine.Repeation(1), 1)
        self.assertEquals(VendingMachine.Repeation(2), 3)
        self.assertEquals(VendingMachine.Repeation(3), 2)

if __name__ == '__main__':
    unittest.main()