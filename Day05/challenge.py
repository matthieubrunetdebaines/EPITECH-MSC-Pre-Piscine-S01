import time
startingTime = time.time()


import random
liste1=sorted([random.randint(0, 1000000) for x in range(1000000)])

# Deuxieme méthode: 

# import random

# liste1 = []

# for i in range (1000000):
#     liste1.append(random.randint(0, 1000000))

# liste1.sort()

duration = time.time() - startingTime
print(duration)



