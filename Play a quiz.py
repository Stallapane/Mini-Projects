#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello! Welcome to the Quiz")


# In[2]:


play = input("Do you want to play? ")


# In[5]:


if play.lower() != 'yes':
    quit()
else:
    print('Lets get started')


# In[10]:


score = 0


# In[11]:


answer = input("what is the band that never plays music? ")


# In[12]:


if answer.lower() == "rubber band":
    print("it's correct")
    score += 1
else:
    print("oops you are wrong :)")


# In[13]:


answer = input("Most tensed animal? ")


# In[14]:


if answer.lower() == 'kangaroo':
    print("correct")
    score += 1
else:
    print("oh no! Incorrect answer")


# In[15]:


answer =  input("who is a short mom? ")


# In[17]:


if answer.lower() == 'minimum':
    print("yayy!correct answer")
    score += 1
else:
    print("Incorrect")


# In[18]:


answer = input("what kind of shoes spy wears? ")


# In[20]:


if answer.lower() == 'sneakers':
    print("correct")
    score += 1
else: 
    print("Better luck next time")


# In[24]:


print(f"Your Score is {score}.")


# In[ ]:




