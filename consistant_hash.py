'''consistent_hashing.py is a simple demonstration of consistent
hashing.'''

import bisect
import hashlib

class ConsistentHash:
  '''

  To imagine it is like a continnum circle with a number of replicated
  server points spread across it. When we add a new server, 1/n of the total
  cache keys will be lost. 
  
  ConsistentHash(n,r) creates a consistent hash object for a 
  cluster of size n, using r replicas. 

  It has three attributes. num_machines and num_replics are
  self-explanatory.  hash_tuples is a list of tuples (j,k,hash), 
  where j ranges over machine numbers (0...n-1), k ranges over 
  replicas (0...r-1), and hash is the corresponding hash value, 
  in the range [0,1).  The tuples are sorted by increasing hash 
  value.

  The class has a single instance method, get_machine(key), which
  returns the number of the machine to which key should be 
  mapped.'''

  def __init__(self,num_machines=1,num_replicas=15,servers=None):
    self.num_machines = num_machines
    self.num_replicas = num_replicas
    hash_tuples = [(index,k,my_hash(str(index)+"_"+str(k))) \
               for index,server in enumerate(servers)
               for k in range(int(num_replicas) * int(server.weight)) ]
    self.hash_tuples=self.sort(hash_tuples);

  
  def sort(self,hash_tuples):
    '''Sort the hash tuples based on just the hash values   '''
    hash_tuples.sort(lambda x,y: cmp(x[2],y[2]))
    return hash_tuples
    
  def add_machine(self,server,siz):
    '''This method adds a new machine. Then it updates the server hash
     in the continuum circle '''
    newPoints=[(siz,k,my_hash(str(siz)+"_"+str(k))) \
                   for k in range(self.num_replicas*server.weight)]
    self.hash_tuples.extend(newPoints)
    self.hash_tuples=self.sort(self.hash_tuples);
    
  def get_machine(self,key):
    '''Returns the number of the machine which key gets sent to.'''
    h = my_hash(key)
    # edge case where we cycle past hash value of 1 and back to 0.
    if h > self.hash_tuples[-1][2]: return self.hash_tuples[0][0]
    hash_values = map(lambda x: x[2],self.hash_tuples)
    index = bisect.bisect_left(hash_values,h)
    return self.hash_tuples[index][0]

def my_hash(key):
  '''my_hash(key) returns a hash in the range [0,1).'''
  return (int(hashlib.md5(key).hexdigest(),16) % 1000000)/1000000.0
