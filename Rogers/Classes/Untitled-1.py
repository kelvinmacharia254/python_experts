# class Employee: 
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
        
#     def __str__(self):
#         return f"{self.name}, {self.age}, {self.position}"
    
#     def __str__ (self):
#         return f"{self.name}: {self.age}, {self.position}"

# emp1 = Employee('Rogers', 30, "Backend Developer")
# print(emp1)

class Students: 
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
        
    # def __str__(self):
    #     return f"{self.name}, {self.age}, {self.position}"
    
    # def __str__ (self):
    #     return f"{self.name}: {self.age}, {self.position}"
    
    def __repr__(self):
        return f"Sisi ndio kusema"
    
    def __add__ (self, obj):
        return f'{self.name}, {obj.name}'
    
    def __call__(self):
        return "You called me as a function"

stu1 = Students('Rogers', 30, "Backend Developer")
stu1
stu2 = Students('Kiome', 60, "Frontend Developer")
stu3 = Students('Mugambi', 90, "Internal Developer")
# print(f"{stu1}")
# str(stu1)
# #print(format())
# format(stu1)
print(stu1 + stu2)

# def __add__ (self, obj):
#     return f'{self.name}, {obj.name}'
# print(__add__(1,2,3))

print(stu1())