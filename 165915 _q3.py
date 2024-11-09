class Employee:
    def __init__(self, name, employee_id, salary):

        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):



        print(f"\nEmployee Details:")


        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: ${self.salary:,.2f}")
    
    def update_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
            print(f"Salary updated to ${new_salary:,.2f}")
            return True
        print("Invalid salary amount.")
        return False
    
    def __str__(self):



        return f"{self.name} (ID: {self.employee_id})"



class Department:
    def __init__(self, department_name):



        self.department_name = department_name
        self.employees = []
    
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            print(f"Added {employee.name} to {self.department_name}")
            return True
        print("Employee already in department.")
        return False
    
    def calculate_total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total
    
    def display_total_expenditure(self):
        total = self.calculate_total_salary()
        print(f"\nTotal salary expenditure for {self.department_name}:")
        print(f"${total:,.2f}")
    
    def display_all_employees(self):
        print(f"\nEmployees in {self.department_name}:")
        if not self.employees:
            print("No employees in this department.")
        else:
            for employee in self.employees:
                print(f"\n- {employee}")
    print(f"  Salary: ${employee.salary:,.2f}")

def main():
    # Create a department
    department = Department("Information Technology")
    
    while True:
        print("\n=== Employee and Department Management System ===")
        print("1. Add new employee")
        print("2. Display all employees")
        print("3. Update employee salary")
        print("4. Display total salary expenditure")
        print("5. Display specific employee details")
        print("6. Exit")  
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
      
      
      
                salary = float(input("Enter employee salary: $"))
                if salary > 0:
                    employee = Employee(name, employee_id, salary)
                    department.add_employee(employee)
                else:
                    print("Salary must be greater than 0.")
            except ValueError:
                print("Please enter a valid salary amount.")
                
      
      
      
        elif choice == "2":



      department.display_all_employees()
            
        elif choice == "3":
            if department.employees:
                print("\nSelect employee to update salary:")
                for i, employee in enumerate(department.employees, 1):
                    print(f"{i}. {employee}")
                try:
              emp_index = int(input("Enter employee number: ")) - 1
                    if 0 <= emp_index < len(department.employees):
                        new_salary = float(input("Enter new salary: $"))
                        department.employees[emp_index].update_salary(new_salary)
                    else:
                        print("Invalid employee number.")
                except ValueError:
                    print("Please enter valid numbers.")
            else:
       
       
         print("No employees in department.")
                
        elif choice == "4":
            department.display_total_expenditure()
            
        elif choice == "5":

     if department.employees:
                print("\nSelect employee:")
                for i, employee in enumerate(department.employees, 1):
                    print(f"{i}. {employee}")
 try:




                    emp_index = int(input("Enter employee number: ")) - 1
                    if 0 <= emp_index < len(department.employees):
                        department.employees[emp_index].display_details()
  else:


                        print("Invalid employee number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No employees in department.")
                
        elif choice == "6":
            print("Thank you for using the Employee Management System!")
            break
            
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()