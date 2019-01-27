#!/usr/bin/env python
# coding: utf-8

# In[13]:


n=int(input("Enter the size of an array:"))
print("Enter the elements of an array:")
a=list(map(int,input().split()))
a=sorted(a)
b=max(a)
c=0
for i in range(n):
    if(a[i]==b):
        c+=1
print(a[n-c-1])


# In[ ]:




