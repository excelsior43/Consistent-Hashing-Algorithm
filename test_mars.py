from mars_json import Mars
import unittest

class TestMars(unittest.TestCase):
  '''
  This is a test class to test CompanyShareAnalyzer class
  '''
  def testForConsistancy(self):
    ''' This raises an exception for inconsistant data in file '''
    mars = Mars()
    jsonDate={'a' : 'Hello'}
    mars.send(jsonDate)
    self.assertEqual(jsonDate, mars.receive())
    
if __name__ == '__main__':
    unittest.main()
 
