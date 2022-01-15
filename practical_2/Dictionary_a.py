# Practical AIM             :-  a. Write a Python script to check whether a given key already exists in a dictionary.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git

# create one dictionary
student = {
    'Id': '20cs052',
    'Name': 'Kishan',
    'Age': '19',
    'gender': 'male',
    'skills': ['JavaScripts', 'React', 'c', 'c++', 'Python']
}

print('Name' in student)        #return True because 'Name'(key) is present in dictionary
print('Address' in student)     #return False because 'Address'(key) is present in dictionary
