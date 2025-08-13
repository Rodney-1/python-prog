# Base Class and Instances
class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
        
    def introduce(self):
            print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    @classmethod
    def set_population(cls, population):
        cls.population = population

# Inheritance for student
class Student(Person):
    
     def __init__(self, name, age, student_id):
          super().__init__(name, age)
          self.student_id = student_id

     def study(self):
          print(f"{self.name} is studying.")

     @staticmethod
     def is_adult(age):
              if age >= 18:
                  return True
              else:
                  return False
              
     @classmethod
     def from_string(cls, data_string):
              name, age, student_id = data_string.split(", ")
              return cls(name, int(age), student_id)
          

# Inheritance for teacher
class Teacher(Person):
     def __init__(self, name, age, subject):
          super().__init__(name, age)
          self.subject = subject

     def teach(self):
          print(f"{self.name} is teaching {self.subject}.")

# Demonstration of functionality
if __name__ == "__main__":
    # Create instances of Person, Student, and Teacher
    student1 = Student("Jimmy", 17, "S12345")
    student2 = Student("Rachael", 20, "S6789")
    teacher = Teacher("Lucas", 40, "History")
    student3 = Student.from_string("Alice, 19, S54321")

    # Instant methods
    student1.introduce()
    student1.study()
    student2.introduce()
    student2.study()
    teacher.introduce()
    teacher.teach()


    # Check if the student is an adult
    print(f"Is {student3.name} an adult? {Student.is_adult(student3.age)}")
    
    #Total population
    print(f"Total population:", Person.population)
    
    # Instance vs Class attributes
    print(f"Population from Student class: {Student.population}")
    print(f"Population from Teacher class: {Teacher.population}")
        
