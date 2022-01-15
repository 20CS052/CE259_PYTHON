# Practical AIM             :-  b. Write a Python script to merge two Python dictionaries.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git

student1 = {
    'Id': 'ab123',
    'Name': 'abc',
    'Age': '19'

}
student2 = {
    'gender': 'male',
    'skills': ['JavaScripts', 'React', 'c', 'c++', 'Python']
}
student3=student1.copy()    #copy all elements from student1 dictionary and storing them in student2 dictionary
student3.update(student2)   #update student3 dictionary by adding elements of student2 dictionary
print("\nstudent1 dictionary")
print(student1)
print("\nstudent2 dictionary")
print(student2)
print("\nstudent3 dictionary")
print(student3)