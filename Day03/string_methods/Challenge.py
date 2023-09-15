input_string = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN."


count_cat = input_string.lower().count("cat")+input_string[::-1].lower().count("cat")
# input_string est la string analysée
# pour des soucis de casse on transforme la string analysé en minuscule
# count() compte le nombre d'occurence de la string en parametre
count_garden = input_string.lower().count("garden")+input_string[::-1].lower().count("garden")
count_mice = input_string.lower().count("mice")+input_string[::-1].lower().count("mice")


total_count = count_cat+count_garden+count_mice

print(f'Occurrences of "Cat": {count_cat}')
print(f'Occurrences of "Garden": {count_garden}')
print(f'Occurrences of "Mice": {count_mice}')

print(f"Nombre total d'occurence {total_count}")
