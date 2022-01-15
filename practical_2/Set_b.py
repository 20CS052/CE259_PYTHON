# Practical AIM             :-  b. Write a Python program to remove an item from a set if it is present in the set.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git

set1 = {"kishan", "prince", "preet", "jeet", "hit", "mit", "meet"}
print(set1)
name = input("insert a name to remove from a list")
initial_length = len(set1)
for i in set1:                  #for loop to check input item is present in the set or not?
    if name == i:               #if statement to discard an item if ti is present in the set
        set1.discard(name)
        break
final_length = len(set1)
if initial_length == final_length:
    print("item entered by you is not present inside the list")
else :
    print("item removed successfully from the set")
print(set1)