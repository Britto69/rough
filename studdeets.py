# Initialize an empty dictionary to store student details
students = {}

# Function to add or update student details
def add_or_update_student(reg_no, details):
    students[reg_no] = details
    print(f"Student with Reg no {reg_no} added/updated.")

# Function to search for a student by registration number
def search_student_by_reg_no(reg_no):
    if reg_no in students:
        print("Student Details:")
        for key, value in students[reg_no].items():
            print(f"{key}: {value}")
    else:
        print(f"No student found with Reg no {reg_no}")

while True:
    print("1. Add/Update Student")
    print("2. Search Student by Reg no")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        reg_no = input("Enter student's registration number: ")
        student_details = {
            'name': input("Enter student's name: "),
            'Phone': input("Enter student's phone number: "),
            'Email': input("Enter student's email address: ")
        }
        add_or_update_student(reg_no, student_details)
    
    elif choice == '2':
        reg_no_to_search = input("Enter registration number to search: ")
        search_student_by_reg_no(reg_no_to_search)
    
    elif choice == '3':
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Exiting the program.")
