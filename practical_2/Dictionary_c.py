# Practical AIM             :-  c. Write a Python program to sum all the items in a dictionary.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git

Dict1= {
    'a': 23,
    'b': 12,
    'c': 19,
    'd': 55,
    'e': 76
}

sum=0;                  #initialize sum
for i in Dict1:         #for loop to sum all the items in a dictionary
    sum=sum+Dict1[i]

print(sum)