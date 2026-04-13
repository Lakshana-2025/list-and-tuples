students=()
n=int(input("Enter no.of students"))
for i in range(n):
    s_id=input("Enter student ID:")
    name=input("Enter student name.")
    marks=float(input("Enter student marks:"))
    s=(s_id,name,marks)
    students=students + (s,)
print("\n All student Records:")
for r in students:
    print("ID:",r[0])
    print("Name:",r[1])
    print("Marks:",r[2])
search_id=int(input("Enter student ID:"))
found=False
for s in students:
    if search_id == s[0]:
        print("Student found:",s)
        found=True
if not found :
    print("Student not found")
max_student=students[0]
for s in students:
    if s[2] > max_student[2]:
        max_student=s
print("\n Student with maximum marks:",max_student)
print("\n Students scoring less than 40:")
found = False
for s in students:
    if s[2] < 40:
        print("Student found:",s)
        found=True
if not found :
    print("Student not found")
tot=0
for s in students:
    tot+=s[2]
avg=tot/len(students)
print("\n Student with average marks:",avg)
