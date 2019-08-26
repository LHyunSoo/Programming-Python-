from game import *
import random

class Baseball_game(Game):
      
    #생성자
    def __init__(self, name):
        super().__init__(name)

    #야구게임 실행
    def start(self):
        self.score=0

        print("\n=============================== 야구 게임 ===============================")
        
        #숫자 정하기
        l=random.sample(range(1,9+1),3)     #1 이상 9+1 미만의 3개 값을 리스트 형식으로 반환 (중복 없음)
        computer = "".join(str(i) for i in l[:3])   #computer에 정한 숫자 넣기
        #computer = ""
        #for i in l[:3] :
        #  computer += str(i)

        self.setnum()   #숫자 정할 때 로딩 띄우기
        print("* 힌트 : 세자리 숫자")

        for i in range(1,10+1): #기회 10번
            user=input("\n"+str(i)+"번째 : ")    #입력받기
            self.compare(computer,user)  #입력값과 답 비교

            #결과
            if self.s==3:   #숫자, 위치가 맞는 것이 3개일 경우
                self.hit()      #답이 맞을 경우
                break
            else:           #숫자, 위치가 맞는 것이 3개가 아닐 경우
                self.strike(self.s)   #같은 위치에 맞는 숫자가 있을 경우
                self.ball(self.b)     #다른 위치에 숫자가 있는 경우

        #결과 출력
        self.result(computer)

    #입력값과 답 비교
    def compare(self,computer,user):

        self.s = 0  #strike 갯수
        self.b = 0  #ball 갯수
        for i in range(len(computer)):  #답의 index 0부터 비교
            for j in range(len(user)):  #입력값의 index 0부터 비교
                if computer[i] == user[j]:  #같은 숫자가 있는 경우
                    if i == j:  #같은 자리일 경우
                        self.s+=1   #strike 갯수 +1
                    else:       #같은 자리가 아닌 경우
                        self.b+=1   #ball 갯수 +1

    #같은 자리에 맞는 숫자가 3개일 경우(=숫자를 맞춘 경우)
    def hit(self):
        print("축하합니다!! 숫자를 맞추셨습니다.")
        self.score+=1

    #같은 자리에 맞는 숫자가 있는 경우
    def strike(self,s):
        print("strike: "+str(s))

    #다른 자리에 숫자가 있는 경우
    def ball(self,b):
        print("ball: "+str(b))

    #야구게임 결과
    def result(self,computer):
        print("\n< < 결과  > >")
        if self.score == 1:  #숫자를 맞췄을 경우
            print(self.name+"님, 주어진 10번의 기회 안에 숫자를 맞춰서 3점을 획득하셨습니다.")
            Game.total+=3   #총점 +3
        else:   #숫자를 맞추지 못했을 경우
            print("답은 "+str(computer)+"(이)었습니다.")
            print(self.name+"님, 주어진 10번의 기회 안에 숫자를 맞추지 못하여 실패하셨습니다.")
        print("=========================================================================")