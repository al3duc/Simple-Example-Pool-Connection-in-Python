'''
MIT License

Copyright (c) 2018 Diego Duque

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


from PoolManagerLib import PoolManager
import time
import pymssql 

nConns= 100 # N. connections to load

print("----------Normal connections----------")
start_time = time.time()
for i in range(nConns):    
    conn=pymssql.connect(server='localhost', user='sa', password='123', database='test')
    cursor = conn.cursor()  
    cursor.execute('select * from users;')  
    row = cursor.fetchone()  
    while row:  
        ##print(row)  
        row = cursor.fetchone()  
    conn.close()
print("--- %s seconds ---" % (time.time() - start_time))

print("----------Connection Pool----------")

poolConn= PoolManager.getInstance()
poolConn.setPoolSize(100) # Set max pool size

#A handle is created for the creation of the objects that will be managed in the pool. 
#In this case I use pymssql for this example, although theoretically any object is valid.
def handler():
    return pymssql.connect(server='localhost', user='sa', password='123', database='test')
   
poolConn.setResourceHandler(handler)

start_time = time.time()
for i in range(nConns):    
    conn= poolConn.getResource() # Get a connection
    cursor = conn.cursor()  
    cursor.execute('select * from users;')  
    row = cursor.fetchone()  
    while row:  
        #print(row)  
        row = cursor.fetchone()  
    poolConn.release(conn) #Return the connection to the pool
print("--- %s seconds ---" % (time.time() - start_time))
print("done!!")