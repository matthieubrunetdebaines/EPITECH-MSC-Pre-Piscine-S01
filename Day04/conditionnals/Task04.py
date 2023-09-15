user_int=int(input("Choose an integer please bro"))

if user_int == 42:
    print("OK")
elif user_int <= 21:
    print("OK")
elif user_int%2==0:
    print("OK")
elif (user_int/2)<21:
    print("OK")
elif (user_int%2!=0) and user_int>=45:
    print("OK")
else:
    print("You got wrong, are you dumb?")