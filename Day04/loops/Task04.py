bottles = ""

for bottles in range (99, 0, -1):
    
    if bottles!=1:
        print(f"{bottles} bottles of age appropriate bottles on the wall\nTake on down, pass it around")
    else:
        print(f"{bottles} bottle of age appropriate bottles on the wall\nTake on down, pass it around")

    bottles-=1