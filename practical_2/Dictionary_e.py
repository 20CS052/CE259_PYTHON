# Practical AIM             :-  e. Write a Python script to concatenate following dictionaries to create a new one.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git


# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict1 = {1: 1430, 2: 420}
dict2 = {3: 360, 4: 4540}
dict3 = {5: 550, 6: 6320}
dict4 = {}                          #dict4 with no items
for d in (dict1, dict2, dict3):     #for loop to concatenate all dict1,dict2,dict3 and storing all items in dict4
    dict4.update(d)
print(dict4)