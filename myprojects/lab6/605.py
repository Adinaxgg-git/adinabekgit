#Read one string S . Using any(), check whether S contains at least one English vowel (a, e, i, o, u) in any case. Print Yes or No.
s = input()
vowels = "aeiou"
s = s.lower()
result = any(letter in vowels for letter in s)
if result:
    print("Yes")
else:
    print("No")