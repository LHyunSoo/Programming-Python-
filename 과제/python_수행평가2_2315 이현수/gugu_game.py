from game import *
import random

class Gugu_game(Game):

    #생성자
    def __init__(self, name):
        super().__init__(name)

    #구구단게임 실행
    def start(self):
        self.score=0

        print("\n============================ 구구단 게임 ============================")
        for i in range(1,5+1):  #5문제
            print("\n< "+str(i)+"번째  > ")
            num1 = random.randint(2,9)  #랜덤으로 단 뽑기
            num2 = random.randint(1,9)  #랜덤으로 숫자 뽑기
            user = int(input(str(num1)+" X "+str(num2)+" = "))    #구구단 문제 답 입력
            answer = num1*num2  #구구단 문제의 답

            self.play(user,answer)  #정답인지 아닌지

        self.result(self.score) #구구단게임 결과

    #정답인지 아닌지
    def play(self,user,answer):
        if user == answer:
            print("- - 정답 - -")
            self.score+=1   #답이 맞으면 점수 +1
        else:
            print("- - 오답 - -")

    def result(self,score):
        print("\n< < 결과  > >")
        if score == 5:  #5문제 모두 맞췄을 경우
            print(self.name+"님, 구구단 5문제 모두 맞추셔서 1점을 획득하셨습니다.")
            Game.total+=1   #총점 +1
        else:   #5문제 모두 맞추지 못했을 경우
            print(self.name+"님, 구구단 5문제를 맞추지 못하여 실패하셨습니다.")
        print("=========================================================================")

