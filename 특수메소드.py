#특수메소드.py
class DeletableClass:
    def __del__(self):      #삭제하는 메소드
        print("delete")

d = DeletableClass()
del d

#p203
class Person: 
    def __init__(self, name, age, height):  #
        self.name = name
        self.age = age
        self.height=height

    def __str__(self):  #return 뒤는 string
        return "Person 설명, 이름은 "+self.name+" 키는 "+str(self.height)

    def __len__(self):
        return len(self.name)   #self.name의 글자수
        #return self.height     #170
        #return self.age        #18

    def __getitem__(self,key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None

p=Person("안세수",18,170)
print(p)            #Person 설명, 이름은 철수 키는 170
print(len(p))       #170
print(p['age'])     #18
print(p['unknown']) #None