# numbers = [1,5,-2,0,6]
# print(numbers,"중 가장 큰 값은 ",max(numbers))
# print(numbers,"중 가장 작은 값은 ",min(numbers))
# print(numbers,"합계는 ",sum(numbers))
# print("2의 10승은 ",pow(2, 10))

# pi = 3.141592
# print(pi,"의 소수점 1자리 반올림은",round(pi))
# print(pi,"의 소수점 1자리 반올림은",round(pi,0))
# print(pi,"의 소수점 2자리 반올림은",round(pi,1))
# print(pi,"의 소수점 3자리 반올림은",round(pi,2))
# print(pi,"의 소수점 4자리 반올림은",round(pi,3))
# print(round(2.55,0))    #3.0
# print(round(2.55,1))    #2.6이 아니라 2.5
# print(round(2.55,2))    #2.55

# user_name = input("이름은? ")
# user_age = input("나이는? ")
# print(user_name + "님의 나이는",user_age+"세입니다.")
# say="{0}님의 나이는 {1}세입니다!"
# print(say.format(user_name,user_age))

# pi="3.141592"
# print("문자열 출력: ",pi)
# print("실수 변환 출력: ",float(pi)) #float.parseFloat(pi) in Java
# print(float(pi)+100)
# year = "2019"
# print("올해 연도: ",year)
# print("100년 뒤는",int(year)+100,"년입니다.")   #Integer.parseInt(pi) in Java
# print("숫자를 문자열로 변화하려면 str()을 이용합니다.")
# print("올해는 "+str(year)+"년입니다.")  #String.valueOf(year) in Java

list = ['a','c','b','d']
list.reverse()
print("리스트 항목 순서 뒤집기",list)
list.sort()
print("리스트 항목 정렬하기",list)
list.sort(reverse=True)
print("리스트 항목 역으로 정렬하기",list)
for index,value in enumerate(list):
    print("인덱스",index,"위치의 값은 ",value)

str = "문자열"
print(str)
n=3
# print(str(n)) 

# <변수명에 사용하면 안되는 것>
# keyword
# 내장함수 이름

# 사용자 정의함수
def input(s):
    print(s)

input("현재의 input()함수는 사용자 정의 함수입니다.")