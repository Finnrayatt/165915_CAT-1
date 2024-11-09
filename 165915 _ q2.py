class Student:




    def __init__(self, name, student_id):



        self.name = name
        self.student_id = student_id
        self.assignments = {}





    
    def add_assignment_grade(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        
    
    def display_grades(self):
        print(f"\nGrades for {self.name} (ID: {self.student_id}):")
        if not self.assignments:



            print("No grades recorded yet.")
        else:
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")




                
    
    def __str__(self):
        return f"{self.name}           (ID: {self.student_id})"

class Instructor:
    def __init__(self, name, course_name):


        self.name = name
        self.course_name = course_name
        self.students = []
    
    def add_student(self, student):


        if student not in self.students:
            self.students.append(student)



            print(f"Added student: {student.name}")
            return True



        print("Student already enrolled in the course.")
        return False
    
    def assign_grade(self, student, assignment_name, grade):
        if student in self.students:



            student.add_assignment_grade(assignment_name, grade)
            print(f"Grade assigned to {student.name} for {assignment_name}")
            return True
        print("Student not found in this course.")
        return False




    def display_all_grades(self):



        print(f"\nAll grades for {self.course_name}:")
        if not self.students:
            print("No students enrolled in the course.")
        else:


            for student in self.students:
                student.display_grades()
                print()

def main():
    #  instructor is created here


    instructor = Instructor("Prof. Smith", "Python Programming 101")
    


    while True:
        print("\n=== Online Strathmore Course Management System ===")

        print("1. Add new student")
        print("2. Assign grade")


        print("3. Display all grades")

        print("4. Display specific student's grades")



        print("5. Exit")
        
        choice =    input("\nEnter your choice (1-5): ")
        
        if choice    == "1":
            name = input("Enter student name: ")

            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)



            


             
        elif choice == "2":
            if instructor.students:


                print("\nSelect student:")
                for i, student in enumerate(instructor.students, 1):
                    print(f"{i}. {student}")


                try:
                    student_index = int(input("Enter student number: ")) - 1
                    if 0 <= student_index < len(instructor.students):


                        assignment_name = input("Enter assignment name: ")
                        grade = float(input("Enter grade: "))



                        instructor.assign_grade(instructor.students[student_index], 
                                             assignment_name, grade)
                    else:

                        print("Invalid student number.")
                except ValueError:
                    print("Please enter valid numbers.")
            else:


                print("No students enrolled yet.")
                
        elif choice == "3":


            instructor.display_all_grades()
            
        elif choice == "4":


            if instructor.students:
                print("\nSelect student:")
                for i, student in enumerate(instructor.students, 1):
                    print(f"{i}. {student}")
                try:



                    student_index = int(input("Enter student number: ")) - 1
                    if 0 <= student_index < len(instructor.students):
                        instructor.students[student_index].display_grades()
                    else:



                        print("Invalid student number.")
                except ValueError:



                    print("Please enter a valid number.")
            else:
                print("No students enrolled yet.")
                
        elif choice == "5":
            print("Thank you for using the Strathmore Course Management System!")
            break
            
        else:


            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    
    main()