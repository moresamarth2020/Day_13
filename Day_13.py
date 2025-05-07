#!/usr/bin/env python
# coding: utf-8

# # Python while Loop
# As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

# In[1]:


i = 0
while(i<5):
    print(i)
    i = i + 1


# In[2]:


while(i<40):
    i = int(input("Enter the number:"))
    print(i)


# In[3]:


count = 6
while(count>0):
    print(count)
    count=count-1


# ### Else with While Loop:
# We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

# In[4]:


count = 6
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside else")


# In[5]:


count = -6
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside else")


# In[14]:


count=int(input("Enter Number:"))
while(count>0):
    print(count)
    count=count-1


# In[ ]:




