students = [
    {"id": "S001", "name": "An", "score": 9.0},
    {"id": "S002", "name": "Binh", "score": 8.5},
    {"id": "S003", "name": "Chi", "score": 7.8},
]

def add_student(students):
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    students.append({"id": sid, "name": name, "score": score})
    print("Student added.\n")

def find_student(students, sid):
    for s in students:
        if s["id"] == sid:
            return s
    return None

def display_all_scores(students):
    if not students:
        print("No students in the list.")
        return
    print("All student scores:")
    for s in students:
        print(f"{s['id']} - {s['name']}: {s['score']}")
    avg = sum(s["score"] for s in students) / len(students)
    print("Average score:", avg)

def main():
    while True:
        print("\nClassroom Data Manager")
        print("1. Add new student")
        print("2. Search student by ID")
        print("3. Display all scores")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            sid = input("Enter student ID to search: ")
            student = find_student(students, sid)
            if student:
                print("Found student:", student)
            else:
                print("Student not found.")
        elif choice == "3":
            display_all_scores(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
             # Uncomment the following line to run the mini project in an interactive environment
main()

