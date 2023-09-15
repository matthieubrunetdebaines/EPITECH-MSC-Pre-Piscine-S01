student = {
    "name": "John Doe",
    "academic_year": "Junior",
    "units": [
        {
            "name":"Web Development",
            "credits":3,
            "grade":"A"
        },
        {
            "name":"Network and System Administration",
            "credits":4,
            "grade":"A"
        },
        {
            "name":"JAVA",
            "credits":1,
            "grade":"A"
        }
    ],
    "total_credits": 0,
    "GPA" : 0
}


valid_grades = ["A", "B", "C", "D", "E"]

for unit in student["units"]:
    if not isinstance(unit["credits"], int) or unit["credits"] < 0 or unit["credits"] >5:
        raise ValueError("Les crédits doivent être des entiers positifs, max 5")
    
for unit in student["units"]:
    if unit["grade"] not in valid_grades:
        raise ValueError("La note doit être entre A et E")
    

grade_weight_mapping={
    4: "A",
    3: "B",
    2: "C",
    1: "D",
    0: "E"
}

for unit in student["units"]:
    unit["grade"] = grade_weight_mapping.get(unit["credits"], "E")

total_credits=0
for unit in student["units"]:
    total_credits+=unit["credits"]

student["total_credits"]= total_credits
student["GPA"]= student["total_credits"]/len(student["units"])

print(student)