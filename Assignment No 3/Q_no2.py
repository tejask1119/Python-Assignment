## Write a program to input any alphabet and check whether it is vowel or consonant :

alphabet = input("Enter an alphabet: ")

alphabet = alphabet.lower()

if alphabet in "aeiou":
    print("Vowel")
else:
    print("Consonant")