from game import *
import random

class Updown_game(Game):

    #생성자
    def __init__(self, name):
        super().__init__(name)

    #업다운게임 실행
    def start(self):
        self.score=0

        print("\n============================== 업다운 게임 ==============================")

        #숫자 정하기
        answer=random.randint(1,500)
        self.setnum()   #숫자 정할 때 로딩 띄우기
        print("* 힌트 : 1 ~ 500 범위의 숫자")

        for i in range(1,10+1):
            user=int(input("\n"+str(i)+"번째 : "))

            if user>500:
                print("잘못 입력하셔서 기회 1번을 잃었습니다.")
                continue
            else:
                if user==answer:    #숫자를 맞췄을 때
                    self.correct()          #숫자 맞음
                    break
                elif user<answer:   #입력 값 < 답 경우
                    self.up_plz(user)       #숫자를 높여라
                    continue
                elif user>answer:   #입력 값 > 답 경우
                    self.down_plz(user)     #숫자를 낮춰라
                    continue
        #업다운게임 결과
        self.result()

    #숫자를 맞췄을 때
    def correct(self):
        print("축하합니다!! 숫자를 맞추셨습니다.")
        self.score+=1
    
    #입력 값 < 답 경우
    def up_plz(self,user):
        print("입력한 숫자 "+str(user)+"(이)가 아닙니다.")
        print("* 힌트 : 숫자 ↑")

    #입력 값 > 답 경우
    def down_plz(self,user):
        print("입력한 숫자 "+str(user)+"(이)가 아닙니다.")
        print("* 힌트 : 숫자 ↓")

    #업다운게임 결과
    def result(self):
        print("\n< < 결과  > >")
        if self.score == 1:  #숫자를 맞췄을 경우
            print(self.name+"님, 주어진 10번의 기회 안에 숫자를 맞춰서 2점을 획득하셨습니다.")
            Game.total+=2   #총점 +2
        else:   #숫자를 맞추지 못했을 경우
            print(self.name+"님, 주어진 10번의 기회 안에 숫자를 맞추지 못하여 실패하셨습니다.")
        print("=========================================================================")