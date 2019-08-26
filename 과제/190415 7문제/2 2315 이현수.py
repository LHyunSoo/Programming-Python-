# 숫자를 입력받아 각 자릿수의 합을 구하는 게임
# 331을 입력하면, 7 출력
# 10을 입력하면, 1 출력

num = input("숫자를 입력하시오. : ")

i = len(num)
sum=0
for x in range(i):
    sum += int(num[x])
print("각 자릿수의 합 : ",sum)

# if len(num) ==3:
#     print("각 자릿수의 합 : ",int(num[0])+int(num[1])+int(num[2])) 
# elif len(num) ==2:
#     print("각 자릿수의 합 : ",int(num[0])+int(num[1]))