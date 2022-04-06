class Student():
    def __init__(self,id,name):
        self.student_id=id
        self.student_name=name
    def newattr(self,c):
        self.student_class=c
    def get(self):
        print("Student ID: ",self.student_id)
        print("Student Name: ",self.student_name)
        print("Student Class: ",self.student_class)
        
a=Student("101","Jacqueline Barnett")
a.newattr("VII")
a.get()