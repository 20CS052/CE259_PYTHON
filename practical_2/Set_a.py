# Practical AIM             :-  a. Write a Python program to add member(s) in a set and clear a set
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git

#A new empty set
Fruits_basket = set()
print(Fruits_basket)
print("\nAdding one element:")
Fruits_basket.add("apple")      #adding one element in set using .add()
print(Fruits_basket)
print("\nAdding multiple items:")
Fruits_basket.update(["orange","mango","banana","grapes"])      #adding multiple element in set using .update()
print(Fruits_basket)
print("\nclearing the Fruits_basket set")
Fruits_basket.clear()       #clearing set using .cleare()
print(Fruits_basket)