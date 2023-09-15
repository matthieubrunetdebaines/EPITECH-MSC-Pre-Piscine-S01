first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
magic = [* zip ( first_name , last_name [:: -1]) ]
print ( magic [0])
print ( magic [3])
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])

# zip() associe les élements correspondant des deux listes et crée un objet pour chaque combinaison
# * permet de décompacter la séquence du résultat