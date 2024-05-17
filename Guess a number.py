#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random


# In[10]:


# we will first ask the user to give a number


# In[11]:


top_of_range = input("give a number: ")


# In[12]:


# we will check if the input given by the user is a number and if it is, is it greater than 0.


# In[13]:


if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("enter a number greater than 0")
        quit()
else:
    print('Please enter a valid number')
    quit()
    


# In[14]:


random_number = random.randint(0,top_of_range)


# In[15]:


guesses = 0


# In[16]:


while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You guessed a higher number")
    else:
        print("You guessed a lower number")
print("you got it in", guesses, "guesses")
        
        


# In[ ]:




