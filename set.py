#Unordered, mutable, unique elements

#Define a set of students
students = {"Gints", "Nauris", "Edgars", "Alise", "Dana", "Anita"}
print("Studentu saraksts: ", students)

#Add a new student
students.add("Diāna")
print("\nPapildinātais studentu saraksts: ", students)

#Add a new student (dublicate)
students.add("Diāna")
print("\nPapildinātais studentu saraksts (atkārtoti): ", students)

#Remove a student
students.remove("Nauris")
print("\nIzmainītais studentu saraksts: ", students)

#Check membership
print("\nVai Alise ir?", "Alise" in students)

#Perform set operations
core_students = {"Gints", "Edgars", "Alise", "Dana", "Anita", "Diāna"}
elective_students = {"Jānis", "Diāna"}

#Students that are either core or elective
all_students = core_students.union(elective_students)
print("\nStudenti, kas ir vai Core vai Elective:", all_students)

#Students that are both core and elective
common_students = core_students.intersection(elective_students)
print("\nStudenti, kas ir Core un Elective:", common_students)