"""
When we add a new server, 1/n of the total cache keys will be lost.
Secondly the *the best output* of this program also depends on the number
of replications. In this scenario I used 15 replications.
"""

import random
import string
import memcache
from consistent_hash import ConsistentHash

class MemcacheClient(memcache.Client):
    """ A memcache subclass. It currently allows you to add a new host at run
time.

only 1/N th cache is wiped out, where N is the number of cache servers.
"""
    def __init__(self, replicas=1,*args, **kwargs):
        self.consistent_hash=ConsistentHash(replicas=replicas)
        super(MemcacheClient, self).__init__(*args, **kwargs)
        

    def _get_server(self, key):
        """ Current implementation of Memcac he client"""
        for i in range(memcache.Client._SERVER_RETRIES):
          server = self.buckets[self.get_server_index(key)]
          if server.connect():
            return server, key
          return None, None
        
    def set_servers(self, servers):
        ret=super(MemcacheClient, self).set_servers(servers)
        self.consistent_hash.setup_servers(servers=self.servers)
        return ret
   
    def get_server_index(self,key):
        '''Returns the number of the machine which key gets sent to.'''
        return self.consistent_hash.get_machine(key)
        

    def add_server(self, server):
        """ Adds a host at runtime to client"""
        # Create a new host entry
        server = memcache._Host(
            server, self.debug, dead_retry=self.dead_retry,
            socket_timeout=self.socket_timeout,
            flush_on_reconnect=self.flush_on_reconnect
        )
        # Add this to our server choices
        self.servers.append(server)
        # Update our buckets
        self.buckets.append(server)
        self.consistent_hash.add_machine(server,len(self.servers)-1)

def random_key(size):
    """ Generates a random key """
    return ''.join(random.choice(string.letters) for _ in range(size))


if __name__ == '__main__':
    # We have 7 running memcached servers
    servers = ['127.0.0.1:1121%d' % i for i in range(1,8)]
    # We have 100 keys to split across our servers
    keys = [random_key(10) for i in range(100)]
    # Init our subclass
    client = MemcacheClient(replicas=15,servers=servers)
    # Distribute the keys on our servers
    for key in keys:
        client.set(key, 1)

    # Check how many keys come back
    valid_keys = client.get_multi(keys)
    print '%s percent of keys matched' % ((len(valid_keys)/float(len(keys))) * 100)

    # We add another server...and pow!
    client.add_server('127.0.0.1:11218')
    print 'Added new server'

    valid_keys = client.get_multi(keys)
    print '%s percent of keys stil matched' % ((len(valid_keys)/float(len(keys))) * 100)
