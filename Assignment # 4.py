#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Question number 1

print("Please select an operation to perform")
print("1 or + to Add")
print("2 or - to Subtract")
print("3 or * to Multiply")
print("4 or / to Divide")
operation = input("Select an operator ")
if operation == "1":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = float(num1)
    num2 = float(num2)
    print("the addition is " + str(num1 + num2))
elif operation == "2":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = float(num1)
    num2 = float(num2)
    print("the subtraction is " + str(num1 - num2))
elif operation == "3":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = float(num1)
    num2 = float(num2)
    print("the product is " + str(num1 * num2))
elif operation == "4":
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = float(num1)
    num2 = float(num2)
    print("the division is " + str(num1 / num2))
else:
    print("Invalid Entry")


# In[4]:


# Question number 2

list = ["abc", "def", 4, "ghi"] 
for x in list: 
    if type(x) == int: 
        print(x)
        break
else:
    print("No, there isn't any numeric value")


# In[5]:


# Question number 3

Dictionary = {
    "1": "100",
    "2": "200",
}
Dictionary["3"] = "300"
print(Dictionary)


# In[8]:


# Question number 4

dict = {
    "data1":100,
    "data2":54,
    "data3":247,
}
print(sum(dict.values()))


# In[36]:


# Question number 5

from collections import Counter
 
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)


# In[40]:


#Question number 6

d = {
     1: 100, 
     2: 200, 
     3: 300, 
     4: 400,
     5: 500,
}

def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(4)


# In[ ]:




