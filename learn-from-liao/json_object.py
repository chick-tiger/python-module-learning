import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s = Student('Bob', 20, 80)
std = json.dumps(s, default=lambda obj:obj.__dict__)
print(std)
reb = json.loads(std,object_hook=lambda d:Student(d['name'],d['age'],d['score']))
print(reb)
