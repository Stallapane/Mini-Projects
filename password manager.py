#!/usr/bin/env python
# coding: utf-8

# In[16]:


from cryptography.fernet import Fernet


# In[17]:


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# In[18]:


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# In[19]:


key = load_key()
fer = Fernet(key)


# In[20]:


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user,passw = data.spli('|')
            print("user:", user, "| passwd:", fer.decrypt(passw.encode()).decode())


# In[21]:


def add():
    name = input('Account Name: ')
    pwd = input('password: ')
    
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# In[22]:


while True:
    mode = input("would you like to add a new password or view type add/view/q to quit: ").lower()
    
    if mode == "q":
        break
    if mode == "view":
        view()
    if mode == "add":
        add()
    else:
        print("Enter a valid mode.")
        continue 
    


# In[ ]:




