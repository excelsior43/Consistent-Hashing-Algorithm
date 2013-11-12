from mars_json import Mars
import io
import unittest

class TestMars(unittest.TestCase):
  '''
  This is a test class to test Mars class
  '''
  def setUp(self):
    self.mars = Mars()

  def testForSendAndRecieveJson(self):
    ''' This raises an exception for inconsistant data in file '''
    
    jsonDate={'a' : 'Hello'}
    self.mars.send(jsonDate)
    self.assertEqual(jsonDate, self.mars.receive())
    
  def testForWritingNonDictionary(self):
    ''' This raises an exception when we try to write a
    non dictionary data into a file'''
    jsonDate="hello" 
    self.assertRaises(Exception, lambda: self.mars.send(jsonDate))
    
  def testForReadingNonDictionary(self):
    ''' This raises an exception when we try to read a
    non dictionary data from a file'''
    with io.open('jsonFile.json', 'w', encoding='utf-8') as f:
        f.write(unicode("Some Non Dictionary data"))
    self.assertRaises(Exception, lambda: self.mars.receive())
    

if __name__ == '__main__':
    unittest.main()
 
