class Student:
    school="Akirachix"
    def __init__(self,firstname,lastname,age,country):
        self.first_name=firstname
        self.last_name=lastname
        self.age=age
        self.country=country

    def greet_student(self):
            return f"Hello {self.first_name} {self.last_name} welcome to {self.school}"
    def year_of_birth(self):
         year=2023-self.age
         return f"Hello {self.first_name} you were born in {year}"
    def show_full_name(self):
         return f"{self.first_name} {self.last_name}"
    def show_initials(self):
         intials=self.first_name[0]+ self.last_name[0]
         return intials.upper()


student1=Student(firstname="rita",lastname="kim" ,age=22,country="kenyan")
student3=Student(firstname="joyuese",lastname="kaba" ,age=22,country="rwandan")
student2=Student(firstname="lado",lastname="glo", age=21,country="ugandan")
print(student1.greet_student())
print(student1.year_of_birth())
print(student1.show_full_name())
print(student2.show_initials())
print(student1.show_initials())
print(student3.show_initials())


        

