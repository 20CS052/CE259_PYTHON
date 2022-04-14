# Practical AIM             :-  Lapindrome.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git


T = int(input())
# for loop for taking T inputs.
for i in range(T):
    n = input()
    L = len(n)
    # condition for checking given input contains odd/even characters.
    if L % 2 == 0:
        b = n[:L // 2]
        c = n[L // 2:]
    else:
        b = n[:L // 2]
        c = n[L // 2 + 1:]
    # given string is Lapindrome if sorted b and sorted c are equal.
    if sorted(b) == sorted(c):
        print("YES")
    # given string is not Lapindrome if sorted b and sorted c are not equal.
    else:
        print("NO")
