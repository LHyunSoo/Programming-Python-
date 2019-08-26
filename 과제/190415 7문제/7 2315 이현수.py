# < 야구 게임 >
# 512가 정답이라면
# 321 2볼
# 312 2스트라이크
# 412 2스트라이크
# 512 3스트라이크 끝!!

import random

#세자리 중복없는 임의의 수 만들기
l=random.sample(range(1,9+1),3)
computer = "".join(str(i) for i in l[:3])

#무한반복
while True:

    #사용자 입력을 받기 input()
    player = input("숫자 세자리를 맞추시오. : ")
    strike = 0
    ball = 0

    #strike, ball 판정하기
    for i in range(len(computer)):
        for j in range(len(player)):
            if computer[i] == player[j]:
                if i == j:
                    strike+=1
                else:
                    ball+=1

    #사용자가 입력한 것, strike, ball 출력하자 print()
    print("{}\tstrike : {}\tball : {}".format(player,strike,ball))
    #임의의 수랑 사용자 입력한게 같으면 HIT   break, if
    if computer == player:
        print("HIT")
        break
