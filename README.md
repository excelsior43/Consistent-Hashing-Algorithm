Assignment
==========

1. Performance :
  Things that enhance the performance of any website :
    1.  Use a good event based webserver, rather that a thread based.
    2.  Ensure data is properly cached
    3.  Denormalization of data. No need to have complex db operations, it consumes time.

2. APIs : 
  To improve the quality of service for a heavy weight site like dubizzle, We need to gave good 
RESTful API on the concepts of HATEOAS - hypermedia as the engine of application state


3. Programming :  
    1.  I have used Consistent hashing algorithm<sup>[1]</sup>. The lost keys are 1/n of the total number of keys. This means the successful key fetch will be 6/7 *100 around 85%. <br>Please download this repository and run the following command. I found this blog (http://michaelnielsen.org/blog/consistent-hashing/) very informative for implementing consistent hash, I tailored the available code to solve the assignment. 
```
$ [sudo] python mamcache_client.py
```
    2.  Here is the sample function to generate random of 7. 
```python
""" Generating random number between 1..7 
when rand_5() is available """
define rand_7() :
  q = 0
  for i in xrange(7):  
    q+= rand_5()
  return q%7 + 1 
```

    3.  According to the specified requirement, I have writter the Mars class.
```
$ [sudo] python mars_json.py
```
    4.  I have also attached a test case for Mars class.
```
$ [sudo] python test_mars.py
```

<u>Reference for consistent-hashing code :</u>
<br><sub>
[1] <b>Michael Nielsen's blog</b>, http://michaelnielsen.org/blog/consistent-hashing/ </sub>





 
      




    
    
