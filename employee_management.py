import random

employees = {}

def generate_id():
    return f"E{random.randint(100, 999)}"

def add_employee():
    emp_id = generate_id()
    name, age, dept = input("Enter Name, Age, Department: ").split(", ")
    if not name.replace(" ", "").isalpha() or not age.isdigit():
        print("Invalid input!"); return
    employees[emp_id] = {"name": name, "age": int(age), "dept": dept}
    print(f"Added! ID: {emp_id}")

def remove_employee():
    print("Removed!" if employees.pop(input("Enter Employee ID: "), None) else "ID not found!")

def update_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id not in employees: print("ID not found!"); return
    name, age, dept = input("Enter New Name, Age, Department (or - to skip): ").split(", ")
    if name != "-": employees[emp_id]["name"] = name
    if age.isdigit(): employees[emp_id]["age"] = int(age)
    if dept != "-": employees[emp_id]["dept"] = dept
    print("Updated!")

def display_employees():
    for id, d in employees.items(): print(f"{id}: {d['name']}, {d['age']}, {d['dept']}")

menu = {
    "1": add_employee, "2": remove_employee, "3": update_employee, 
    "4": display_employees, "5": exit
}

while True:
    menu.get(input("\n1.Add 2.Remove 3.Update 4.Display 5.Exit\nChoice: "), lambda: print("Invalid!"))()
