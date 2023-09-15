user_int = int(input("Choose an int: "))
user_str= str(input("Write your string: "))

vowels=["a", "e", "i", "o", "u", "y"]
user_str_lower=user_str.lower()

vowels_found= False

if user_int==0:
    quit()

for char in user_str_lower:
    if char in vowels:
        vowels_found= True
        break

if vowels_found:
    print(user_int)

elif user_int>=42:
    print(user_int)

else:
    print(user_str)