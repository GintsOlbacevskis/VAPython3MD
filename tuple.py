#Ordered, immutable, allows dublicates

#Define a tuple representing a student record
student_record = ("Gints", 35, "70")

#Access elements in the tuple
print("Vārds:", student_record[0])
print("Vecums:", student_record[1])
print("Atzīme:", student_record[2])

#Use tuples to return multiple values from a function
def calculate_stat(grades):
    averge = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    return (averge, highest, lowest)

#Example usage
grades = [85, 90, 78, 92]
stats = calculate_stat(grades)
print(f"Vidēji: {stats[0]}, Augstākā: {stats[1]}, Zemākā: {stats[2]}")