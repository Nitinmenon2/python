#!/usr/bin/env python
# coding: utf-8

# # Leap Year Or Not
# 

# In[2]:


n = int(input("Enter the year"))
if n%4 == 0:
    print("Leap year")
else:
    print("Not a Leap Year")


# # Week and Day

# In[3]:


weekNumber = input("Enter the week number:")
weekNumber = int(weekNumber)
if (weekNumber == 1):
  weekDay = "Saturday"
elif (weekNumber == 2):
  weekDay = "Sunday"
elif (weekNumber == 3):
  weekDay = "Monday"
elif (weekNumber == 4):
  weekDay = "Tuesday"
elif (weekNumber == 5):
  weekDay = "Wednesday"
elif (weekNumber == 6):
  weekDay = "Thursday"
elif (weekNumber == 7):
  weekDay = "Friday"
else:
  weekDay = "Please enter the week number between 1 and 7" 
print(weekDay)
  


# # The largest of three numbers

# In[5]:


n1 = int(input("enter first"))
n2 = int(input("enter second"))
n3 = int(input("enter third"))

if (n1>n2) and (n1>n3):
        print ("n1 is big")
elif (n2>n1) and (n2>n3):
        print ("n2 is big")
else:
        print ("n3 is big")


# # Sum of series upto n

# In[11]:


num = int(input("enter the limit"))
sum = 0
while(num > 0):
       sum += num
       num -= 1
       print("The sum is",sum)


# # Sum and Average of given series of numbers

# In[2]:


n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))
sum=0
avg=0.0
sum = (n1+n2)
avg = (n1+n2)/2
print("sum is",sum)
print("avg is",avg)


# # Roots of Quadratic Equations AX2+BX+C=0

# In[3]:


a = int(input("enter a value"))
b = int(input("enter b value"))
c = int(input("enter c value"))
sol1=0
sol2=0
sol1 = (-b-sqrt(d))/(2*a)
sol2 = (-b+sqrt(d))/(2*a)
print("root1 is",sol1)
print("root2 is",sol2)


# # Divisor for a number

# In[5]:


n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)


# # Celsius to Fahrenheit

# In[6]:


celsius=int(input("Enter the temperature in celsius:"))
f=(celsius*1.8)+32
print("Temperature in farenheit is:",f)


# In[ ]:




