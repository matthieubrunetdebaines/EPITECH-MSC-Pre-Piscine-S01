my_int= -30

for my_int in range(-30, 31) :

    if my_int==0:
        print(my_int)
    elif my_int%3==0 and my_int%5==0:
        print("FizzBuzz")
    elif my_int%3==0:
        print("Fizz")
    elif my_int%5==0:
        print("Buzz")
    else:
        print(my_int)

my_int+=1