liste1=list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))

print(liste1)

liste1.sort()

print(liste1)

list_under_seven=[]

for i in range(len(liste1)-1):
    if liste1[i]<7:
        list_under_seven.append(liste1[i])

print(list_under_seven)