students=[
    [100,"arun","bca",145],
    [101,"aruna","mca",125],
    [102,"arjun","mca",185],
    [104,"arnu","bcom",145],
    [105,"anu","bcom",170]

]
#print student names
for student in students:
    print(student[1])

#list students whose course is mca
for student in students:
    if student[2]=="mca":
        print(student)

#print total of all students
total=0
for student in students:
    total=total+student[3]
print(total)

#mca #bca #bcom
mtotal=btotal=bctotal=0
for student in students:
    if student[2]=="mca":
        mtotal+=1
    elif student[2]=="bca":
        bctotal+=1
    elif student[2]=="bcom":
        btotal+=1
print("mca",mtotal)
print("bca",bctotal)
print("bcom",btotal)

#print max value from list



