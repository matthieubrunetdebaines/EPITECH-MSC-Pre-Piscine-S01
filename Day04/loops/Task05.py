user_int = int(input("choose an integer"))

for multiple in range (2, user_int + 1):

    multiples=[]
    if multiple<=(user_int/2):
        multiples.append(multiple)
        
    for j in range(2, user_int):
        if multiple * j < user_int:
            multiples.append(multiple*j)

    multiples.sort(reverse=True)

    if multiples:
        print(multiples)