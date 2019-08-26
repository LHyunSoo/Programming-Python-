# < 자리배치 >
# 우리반 번호와 임의의 숫자를 나열한다

# 끝번호를 입력하세요: 20
# 제외할번호 입력하세요: 15 
# 제외할번호 입력하세요: 19
# 자리  학생번호
# 1		19
# 2		7
# 3		3
# ...
import random
 
print("< 자리배치 >")

last = int(input("끝번호를 입력하세요. : "))
student= list(range(1,last+1))

delStu = int(input("제외할 학생의 수를 입력하세요. : "))
for i in range(delStu):
    delNum = int(input("제외할 번호를 입력하세요. : "))
    student.remove(delNum)

random.shuffle(student)

print("자리\t학생번호")
for i in range(1,len(student)):
    print(i,"\t",student[i-1])
 