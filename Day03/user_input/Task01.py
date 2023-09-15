# Ask the user for their name
user_name = input("What is your name? ")
first_letter=user_name[0].capitalize()

# Greet the user
print(f"Hello, {first_letter}{user_name[1:]}!")