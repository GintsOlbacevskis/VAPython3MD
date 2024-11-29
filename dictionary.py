#Key-value pairs, mutable, keys unique

#Define a dictionary of student grades
grades = {"Gints": 70, "Nauris": 90, "Edgars": 67, "Alise": 75, "Dana": 91, "Anita": 78}
print("Studentu atzīmju saraksts: ", grades)

#Add a new student grade
grades["Diāna"] = 89
print("\nPapildinātais studentu atzīmju sarakstam: ", grades)

#Update a grade
grades["Gints"] = 82
print("\nIzmainītais studentu atzīmju saraksts: ", grades)

#Retrieve a special grade
print("\nAlise atzīme: ", grades["Alise"])

#Iteral through the distionary
print("\nVisu studentu atzīmes:")
for student, grade in grades.items():
    print(f"{student}: {grade}")