class Student:
    def __init__(self,roll_no,name,python_marks,ds_marks,cn_marks):
        self.roll_no=roll_no
        self.name=name
        self.python_marks=python_marks
        self.ds_marks=ds_marks
        self.cn_marks=cn_marks

    def display(self):
        print(self.roll_no,self.name,self.python_marks,self.ds_marks,self.cn_marks)

    def __del__(self):
        print('Deleted constructor')

s0=Student(2002078,'Abhi',90,80,85)
s0.display()
s1=Student(2002029,'Himanshu',50,45,35)
s1.display()
s2=Student(20020241,'XYZ',100,95,65)
s2.display()
del s2
