student = {
    "name": "Hiraj",
    "age": 20,
    "course": "BSCSE",
    "marks": 95,
    "status":"single"
}
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

student["marks"] += 5
if student ["marks"] >=40:
    student["status"] = "pass"
else:
    student["status"] = "fail"

print("dictionary")
print(student)