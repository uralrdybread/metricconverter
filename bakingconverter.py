
# coding: utf-8

# In[7]:


print("How many cups of bread flour would you like to convert to grams?")
cups = input()

grams = float(cups)*130

grams = round(grams, 2)
#This rounds to the nearest hundredths place for more accuracy

print(f"{cups} cups is equal to {grams} grams ")

