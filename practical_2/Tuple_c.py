# Practical AIM             :-  c. Write a Python program to add an item in a tuple.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git

#create a tuple
tuple3 = (4, 6, 2, 8, 3, 1)
print(tuple3)

#tuples are immutable
#add an element using + operator and storing it in tuple4
tuple4 = tuple3 + (9,)
print(tuple4)

#adding items in a specific index
tuple5 = tuple3[:5] + (15, 20, 25)
print(tuple5)

#converting the tuple to list
list1 = list(tuple3)
#add an element in list using append
list1.append(30)
tuple6 = tuple(list1)   #converting list in tuple
print(tuple6)