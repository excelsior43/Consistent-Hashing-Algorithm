''' Mars class is used to do simple file json read and write operations'''
import io
import json

class Mars(object):
  ''' This class initializes using a file name as the arguement.
  send(json): writes json to a file
  read(): reads json from a file
  '''
  def __init__(self, fileName="jsonFile.json"):
    ''' This function take a file name as an arguement 
    This method truncates the initialized file'''
    self.fileName = fileName
    with io.open('jsonFile.json', 'w', encoding='utf-8') as f:
        f.truncate()

  def send(self, data):
    ''' take a dictionary as arguement and writes it to the file
    this throws a Exception on error'''
    if not isinstance( data, dict ):
      raise Exception (" %r is not a dict" %( data)) 
    try :
      with io.open(self.fileName, 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))
        return 1
    except Exception as e:
        raise e
    
  def receive(self):
    ''' receive() reads the file and returns a json object.
    This method throws a ValueError, if the data loded is not
    of type dictionary'''
    try :
      with open(self.fileName, 'r') as json_file:
        data = json.load(json_file)
        return data
    except Exception as e:
      raise e
