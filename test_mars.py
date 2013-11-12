from mars_json import Mars
import io
import unittest

class TestMars(unittest.TestCase):
  '''
  This is a test class to test CompanyShareAnalyzer class
  '''
  def setUp(self):
    with io.open('jsonFile.json', 'w', encoding='utf-8') as f:
        f.truncate()

  def testForSendAndRecieveJson(self):
    ''' This raises an exception for inconsistant data in file '''
    mars = Mars()
    jsonDate={'a' : 'Hello'}
    mars.send(jsonDate)
    self.assertEqual(jsonDate, mars.receive())
    
  def testForWritingNonDictionary(self):
    ''' This raises an exception when we try to write a
    non dictionary data into a file'''
    mars = Mars()
    jsonDate="hello"
    self.assertRaises(Exception, lambda: mars.send(jsonDate))
    
  def testForReadingNonDictionary(self):
    ''' This raises an exception when we try to read a
    non dictionary data from a file'''
    with io.open('jsonFile.json', 'w', encoding='utf-8') as f:
        f.write(unicode("Some Non Dictionary data"))
    mars = Mars()
    self.assertRaises(Exception, lambda: mars.receive())
    

if __name__ == '__main__':
    unittest.main()
 
