"""
创建一个学生Student类，具有姓名，年龄等数据
    具有学习，工作等行为
"""

class Student:
    def __init__(self,name,age,sex,phone):
        self.name = name
        self.age = age
        self.sex = sex
        self.phone = phone

    def xuexi(self):
        print(self.name + "zai xue xi!")

s01 = Student('weimin','100','nan','18172390395')
print(s01.name)
s01.xuexi()
