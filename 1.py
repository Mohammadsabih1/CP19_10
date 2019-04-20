#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program (id shape)
#Written By (Mohammad Sabih)

n=int(input("enter number="))
def triangle_pattren():
	for i in range(1,n):
    		for j in range(1,n-i):
        		print(" ",end=" ")
    		for j in range (1,1*i):
        		print("8","3",end=" ")
   	 	print("8")
triangle_pattren()

