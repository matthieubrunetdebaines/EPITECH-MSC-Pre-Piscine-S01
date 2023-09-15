liste1 = []
list_element=1

for i in range(10):
    liste1.append(list_element)
    list_element+=1

print(liste1)

list_multip=liste1[0]

for i in range(len(liste1)):
    list_multip=liste1[i]*list_multip

print(list_multip)