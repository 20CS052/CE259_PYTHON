# Practical AIM             :-  Find Captain Room Number.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git


k = int(input())
rooms = list(map(int, input().split())) #List of integers, taking integers in spaces
a = set()
b = set()

for room in rooms:
    if room not in a:       #if room is not in a then it will
        a.add(room)         #add that integer in a and b
        b.add(room)
    else:                   #now if room is already in a then
        b.discard(room)     #it will discart that int from b
b = list(b)                 #convert b into list
print(b[0])
