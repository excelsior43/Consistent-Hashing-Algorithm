dub
===

1. Performance :
  Things that enhance the performance of any website :
    1) using a good event ased webserver, rather that a thread based.
    2) Proper caching of data 
    3) Denormalization of data.. No need to have complex db operations... 

2. APIs : 
  To improve the quality of service for a heavy weight site like dubizzle, We need to gave good 
RESTful API on the concepts of HATEOAS - hypermedia as the engine of application state


3. Programming : 
    1.  I have used continuous hashing algorithm. 
    2.  Here is the sample function to generate random 7


```python
define rand_7() :
  q = 0
  for i in xrange(7):  
    q+= rand_5()
  return q%7 + 1 
```



 
      




    
    
