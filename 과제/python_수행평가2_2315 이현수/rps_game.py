from game import *
import random

class Rps_game(Game):
    
    #생성자
    def __init__(self, name):
        super().__init__(name)

    #가위바위보게임 실행
    def start(self):
        self.score=0

        print("\n========================== 가위바위보 게임 ==========================")
        for i in range(1,5+1):  #5번
            print("\n< "+str(i)+"번째  > ")
            user=int(input("어떤 걸 내시겠습니까?(1: 가위\t2: 바위\t3: 보): "))
            computer = random.randint(1,3)  #유저가 낼 것 입력받기

            if user >= 1&user<=3:   #가위, 바위, 보 중에 입력했을 경우
                self.play(user,computer)    #가위바위보하기
            else:   #잘못입력한 경우
                print("잘못입력하셨으므로 기회를 잃었습니다.")
                continue
            
        self.result()   #가위바위보게임 결과

    #가위바위보하기
    def play(self,user,computer):
        #가위, 바위, 보 선택할 수 있게 리스트를 만듬
        rps = ["가위","바위","보"]

        #유저와 컴퓨터가 낸 것
        print("\n"+self.name+": "+rps[user-1])
        print("컴퓨터: "+rps[computer-1])

        #가위바위보할 때 마다 알려주는 결과
        
        print("- 결과 -")
        if user ==1:   #유저: 가위
            if computer==1:     #컴퓨터: 가위
                self.draw()         #비김
            elif computer == 2: #컴퓨터: 바위
                self.lose()         #유저 패
            elif computer==3:  #컴퓨터: 보
                self.win()          #유저 승
                self.score+=1       #점수 +1
        elif user==2:   #유저: 바위
            if computer==1:     #컴퓨터: 가위
                self.win()          #유저 승
                self.score+=1       #점수 +1
            elif computer == 2: #컴퓨터: 바위
                self.draw()         #비김
            elif computer==3:  #컴퓨터: 보
                self.lose()         #유저 패
        elif user==3:   #유저: 보
            if computer==1:     #컴퓨터: 가위
                self.lose()         #유저 패
            elif computer == 2: #컴퓨터: 바위
                self.win()          #유저 승
                self.score+=1       #점수 +1
            elif computer==3:  #컴퓨터: 보
                self.draw()         #비김
        
    #비겼을 때
    def draw(self):
        print("비겼습니다.")
    #이겼을 때
    def win(self):
        print(self.name+" 승리")
    #졌을 때
    def lose(self):
        print("컴퓨터 승리")

    #가위바위보게임 결과
    def result(self):
        print("\n< < 결과  > >")
        if self.score >= 2:  #2번 이상 이겼을 경우
            print(self.name+"님, 가위바위보 2번이상 이겼으므로 2점을 획득하셨습니다.")
            Game.total+=2   #총점 +2
        else:   #2번 이상 이기지 못했을 경우
            print(self.name+"님, 가위바위보 2번이상 이기지 못하여 실패하셨습니다.")
        print("=========================================================================")