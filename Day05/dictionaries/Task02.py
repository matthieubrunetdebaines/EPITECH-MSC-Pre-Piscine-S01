student = {
    "name": "John Doe",
    "academic_year": "Junior",
    "units": [
        {
            "name":"Web Development",
            "credits":2,
            "grade":"D"
        },
        {
            "name":"Network and Sustem Administration",
            "credits":5,
            "grade":"A"
        },
        {
            "name":"JAVA",
            "credits":4,
            "grade":"B"
        }
    ]
}

valid_grades = ["A", "B", "C", "D", "E"]

for unit in student["units"]:
    if not isinstance(unit["credits"], int) or unit["credits"] <= 0 or unit["credits"] >5:
        raise ValueError("Les crédits doivent être des entiers positifs, max 5")
    
for unit in student["units"]:
    if unit["grade"] not in valid_grades:
        raise ValueError("La note doit être entre A et E")
    
print(student)