#!/usr/bin/env python
# coding: utf-8

# In[2]:


number = input()
string = ''
buf = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 
       'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']#Создал список букв+пробел

if number == 'End' :
    print()
else : 
    number = int(number)

while number != 'End' :
    number = int(number)
    string += buf[number]
    number = input()

print(string)   


# In[ ]:




