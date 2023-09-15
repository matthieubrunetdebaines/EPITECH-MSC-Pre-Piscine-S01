

# pi = 3 + (1**2)/(6+(3**2))/(6+(5**2))/(6+(7**2))

# total = 0
# n = 1

# for _ in range(1000000):
#     step = (n**2)/(6+((n+2)**2))
#     n += 2

# result = step + 3

# pi_approximation = round(result, 6)

# print("Approximation de Pi avec 6 décimales de précision :", pi_approximation)


# n = 3
# pi = 3

# def first_step(n) :
#     result_function = (6 + ((n ** 2)/((n+2)**2)))
#     return result_function

# for _ in range(100000):
#     first_step(n)
#     n += 2



# pi += 1/first_step

# pi_approximation = round(pi, 6)
# print(first_step)

# !!!!!!!!!!!!!!!!!!!

# def dividende (n) :
#     div = 6+(n ** 2)
#     return div

# pi = 3
# n = 3
# pis= 0

# for _ in range(1000):
#     pis += (dividende(n)/(dividende(n+2)))
#     n += 2

# pi += 1 / pis

# print(pi)

# def calculate_pi(iterations):
#     pi = 0
#     n = 1

#     for _ in range(iterations):
#         term = 1 / (6 + (n ** 2) / (6 + (n + 2) ** 2))
#         pi += term
#         n += 2

#     return pi

# iterations = 1000  # Nombre d'itérations pour la précision
# pi_approximation = 3 + calculate_pi(iterations)

# pi_approximation = round(pi_approximation, 6)
# print("Approximation de Pi avec 6 décimales de précision :", pi_approximation)


# def step_one (step_one(n)) :
#     res_step_one = (6+(n**2))
#     return res_step_one

# def step_one (step_one(5)):
#     for _ in range (10) :
#         div = step_one(n-2)/step_one(n)
#         n+=2

#     return div

# Pi = 3 + 1/(step_one(5))

# print(Pi)

# !!!!!!!!!!!!!!!!!!!!!!!!


# def calculate_pi(n, iterations):
#     if iterations == 0:
#         return 0
#     else:
#         term = (n ** 2) / (6+calculate_pi(n + 2, iterations - 1))
#         return 6 + term

# # Précision souhaitée (le nombre de fois que la formule sera répétée)
# precision = 700  # Augmentez pour une meilleure précision

# # Valeur de départ pour n
# n_start = 0

# # Calcul de Pi en utilisant la formule récursive
# pi_approximation = calculate_pi(n_start, precision)

# # Divise 1 par le résultat et ajoute 3
# pi_approximation = 3 + 1 / pi_approximation

# pi_approximation = round(pi_approximation, 6)
# print("Approximation de Pi avec 6 décimales de précision :", pi_approximation)


# n=3

# a = 3
# b = (1**2)
# # c=(6+((n**2)/(6+((n+2)**2)/(6+((n+4)**2)/...))))


# def calc(n, iterations):
#     res_calc= 1
#     for _ in range (iterations):
#         d=(n)**2
#         res_calc = (6+(d))/(calc(n+2, iterations-1))
#         n+=2

#     return res_calc
    
# iterations = 10
    
# c=calc(3, iterations)

# Pi= a+(b/(c))

# print(Pi)

# !!!!!!!!!!!!!!!!!

n = 5  # Le nombre de termes
total = 0
current_term = 1

for _ in range(n):
    total += current_term
    current_term = current_term * 10 + 1

print(total)
