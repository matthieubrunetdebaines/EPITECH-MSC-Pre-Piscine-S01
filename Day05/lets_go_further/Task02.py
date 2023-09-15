guests= ["Sam", "Frodo", "Merry", "Pippin", "Sam"]

count_in_guests=0

for guest in guests:
    if guests.count(guest)>1:
        guests.remove(guest)

print(guests)