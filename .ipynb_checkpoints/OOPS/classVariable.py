class student:
    school_name = 'RNTU'
    def __init__(self, name , roll_no):
        self.n = name
        self.r = roll_no
        student.school_city = 'bhopal'

    def add_new(self):
        student.school_code = 101
        print(student.school_city, student.school_name, student.school_code,student.contact)
        print(self.n,self.r)



student.contact = 1234566777
obj = student('sharvan' , 123)
obj.add_new()

print(student.contact,student.school_name,student.school_code,student.school_city,)