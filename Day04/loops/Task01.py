user_str=str(input("Write a string: "))

duplicated_string = ""

for char in user_str:
    duplicated_string += char*2

print(f"{duplicated_string}")