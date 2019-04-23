
# coding: utf-8

# In[4]:


file=open("sp199.txt","r")
new=open("newDmFile.txt","w")
print("-------------")
for line in file:
    new.write("***"+line)
file.close()
new.close()

