#!/usr/bin/env python
# coding: utf-8

# In[31]:


number = input()
string = ''
if number == 'End' :
    print()
else : 
    number = int(number)
while number != 'End' :
    number = int(number)
    if number == -1 :
        string += ' '
    elif number >= 0 and (number <= 5) : 
        string += chr(1072 + number)   
    else : 
        string += chr(1071 + number)
    number = input()
print(string)   


# In[24]:


s = input()
for i in range(len(s) + 1) :
    if s[i+1] != ' '


# In[ ]:


18 5 11 20 12 32 17 9 8 0 23 9 32 End

