#Order, mutable, allows duplicates

#Define a list of students
students = ["Gints", "Nauris", "Edgars", "Alise", "Dana", "Anita"]
print("Studentu saraksts: ", students)

#Add a new student
students.append("Diāna")
print("\nPapildinātais studentu saraksts: ", students)

#Remove a student
students.remove("Nauris")
print("\nIzmainītais studentu saraksts: ", students)

#Access a student by index
print("\nPirmais students: ", students[0])

#Iteral through the list
print("\nStudentu saraksts:")
for student in students:
    print(student)