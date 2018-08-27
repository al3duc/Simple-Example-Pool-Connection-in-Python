# Simple Example Pool Connection in Python

###How to use this?

```python

from PoolManagerLib import PoolManager
import pymssql 

poolConn= PoolManager.getInstance()
poolConn.setPoolSize(100) # Set max pool size

#A handle is created for the creation of the objects that will be managed in the pool. 
#In this case I use pymssql for this example, although theoretically any object is valid.
def handler():
    return pymssql.connect(server='localhost', user='sa', password='123', database='test')
   
poolConn.setResourceHandler(handler)


 conn= poolConn.getResource() # Get a connection

 ...

 poolConn.release(conn) #Return the connection to the pool

```