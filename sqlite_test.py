
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create the table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
""")

# Add example students if they don't already exist
cursor.execute(
    "INSERT OR IGNORE INTO students VALUES (?, ?, ?)",
    (1001, "Farheen", 22)
)

cursor.execute(
    "INSERT OR IGNORE INTO students VALUES (?, ?, ?)",
    (1002, "Rahul", 21)
)

connection.commit()

print("\n===== SQLITE STUDENT DATABASE =====")
print("1. View all students")
print("2. Update a student")
print("3. Delete a student")
print("4. Exit")

choice = input("Enter your choice: ").strip()

if choice == "1":
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        print(student)

elif choice == "2":
    student_id = int(input("Enter student ID to update: "))
    new_name = input("Enter new name: ").strip()
    new_age = int(input("Enter new age: "))

    if not new_name:
        print("Name cannot be empty!")
    elif new_age <= 0:
        print("Age must be positive!")
    else:
        cursor.execute(
            "UPDATE students SET name = ?, age = ? WHERE student_id = ?",
            (new_name, new_age, student_id)
        )

        if cursor.rowcount > 0:
            connection.commit()
            print("Student updated successfully!")
        else:
            print("Student not found.")

elif choice == "3":
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    if cursor.rowcount > 0:
        connection.commit()
        print("Student deleted successfully!")
    else:
        print("Student not found.")

elif choice == "4":
    print("Goodbye!")

else:
    print("Invalid choice.")

connection.close()