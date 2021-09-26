#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def pluz(arg1, arg2):
    arg = 'Эти объекты нельзя сложить!'
    try:
        arg = arg1 + arg2
    except Exception :
        pass
    try:
        arg = int(arg1) + arg2
    except Exception :
        pass
    try:
        arg = arg1 + int(arg2)
    except Exception :
        pass
    return arg
print(pluz(arg1, arg2))
# Вместо arg1 и arg2 должны стоять вводные

