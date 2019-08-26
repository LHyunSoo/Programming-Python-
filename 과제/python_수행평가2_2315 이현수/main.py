# 2315 이현수

# <실행 방법>
# 1. main.py 파일을 실행해야한다.
# 2. 게임 설명을 보려면 1, 게임 메뉴를 고르려면 2 선택해야한다.
# 3. 유저의 이름 입력해야한다.
# 4. 게임 메뉴에서 미니게임 4개 중에 게임 선택해야한다.
# 5. 입력란에 기회와 현재 점수가 표시되어 있는 것을 고려하여 게임을 클리어해야한다.
# 6. 기회 3번이 끝나거나 총점 5점을 획득하면 게임 끝이 난다.
# 7. 성공했는지 실패했는지 결과가 출력된다.
# 8. 그만할련지 물어본다.

# <프로젝트 소개>	: 어떤 프로젝트인지 간략하게 소개
# 미니게임 4가지 중 한개씩 선택해 게임을 하여 기회 3번만에 총 점 5점이상이 되어야합니다.
# 난이도에 따라 점수가 달라 점수가 클수록 어렵습니다.

from game import *
from gugu_game import *
from rps_game import *
from updown_game import *
from baseball_game import *

print("< < < Mini Game > > >")
print("1. 게임 설명")
print("2. 게임 메뉴")
c=int(input("선택하시오.>> "))

#일단 name 초기화
g=Game("null")

#다시할수도 있기 때문에 run 생성
run = True

#게임 시작
while(run):
    if c ==1:   #1번 선택        
        g.explain() #게임 설명

    if c==1 or c==2:    #1번이나 2번 선택 
        print("\n<<< 게임 시작 >>>")
        name=input("이름을 입력하시오.>> ")
        g=Game(name)    #이름 등록

        for i in range(3):
            chance=3-i  #남은 기회

            #게임 메뉴
            g.kind()    
            #게임 메뉴 고르기
            cg = int(input("게임을 선택하시오.(기회: "+str(chance)+"번 / 현재 점수: "+str(g.total)+")>> "))
            
            if cg==1:
                gg=Gugu_game(name)  #이름 등록
                gg.start()  #구구단 게임 실행
            elif cg==2:
                rg=Rps_game(name)   #이름 등록
                rg.start()  #가위바위보 게임 실행
            elif cg==3:
                ug=Updown_game(name)    #이름 등록
                ug.start()  #업다운 게임 실행
            elif cg==4:
                bg=Baseball_game(name)  #이름 등록
                bg.start()  #야구 게임 실행
            else:   #잘못 입력했을 경우
                print("잘못 입력하셨습니다. 다시 입력해주세요.")
                i-=1    #기회가 줄지 않아야 하기 때문
                continue
            
            #총점 5점이상일 경우
            if g.total >= 5:
                break

        #게임이 종료되며 최종결과 출력
        g.end() 

    #다시 할건지 물어보고 입력받기
    how=int(input("\n"+g.name+"님 다시 하시겠습니까? (0: 다시 할래요. 1: 그만할래요.)>> "))
    if how==0:      #다시하기
        run==True       #while(True)
    elif how == 1:  #그만하기
        run=False       #while(False)
    else:   #잘못 입력했을 경우
        print("잘못 입력하셨으므로 종료합니다.")
        run=False

print("\n- End -")
