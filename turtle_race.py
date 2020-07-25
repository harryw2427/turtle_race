#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
color=['red','blue','green']
speed=[1,2,3]
turtle0=turtle.Turtle()
turtle1=turtle.Turtle()
turtle2=turtle.Turtle()
turtle2.color(color[2])
turtle_list=[turtle0,turtle1,turtle2]
for i in range(3):
    turtle_list[i].color(color[i])
    turtle_list[i].penup()
    turtle_list[i].goto(-160, 100*i)
    turtle_list[i].pendown()
for turtle in turtle_list:
    turtle.shape('turtle')
from random import randint
for movement in range(100):
    for turtle in turtle_list:
        speed=randint(1,5)        
        turtle.forward(speed)

for turtle in turtle_list:
    print(turtle.pos(),turtle.color())
    
    


# In[ ]:




