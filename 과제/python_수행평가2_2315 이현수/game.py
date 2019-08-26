import time

class Game:
    total = 0
    
    #생성자
    def __init__(self,name):
        self.name = name

    #게임 설명
    def explain(self):
        print("=========================================================================")
        print("< 게임 설명 >")
        print(": 게임을 할 수 있는 횟수 3번만에 총 5점을 획득하면 성공하는 게임입니다.\n")
        print("1. 구구단게임 (1점)")
        print(": 5개의 구구단 문제를 모두 맞춘다면 1점 획득 !")
        print("2. 가위바위보게임 (2점)")
        print(": 가위바위보 5번의 기회 중 2번 이긴다면 2점 획득 !"
                           + "\n 잘못 입력할 시, 기회를 잃음")
        print("3. 업다운게임 (2점)")
        print(": 10번의 기회 중 특정 숫자(1~500)를 맞추면 2점 획득 !")
        print("4. 야구게임 (3점)")
        print(": 10번의 기회 중 특정 세자리 숫자를 맞추면 3점 획득 !")
        print("=========================================================================")

    #게임 메뉴
    def kind(self):
        print("\n< 게임 메뉴 >")
        print("1. 구구단게임 (1점)")
        print("2. 가위바위보게임 (2점)")
        print("3. 업다운게임 (2점)")
        print("4. 야구게임 (3점)")

    #3,4번 게임에 해당
    #숫자 정하기
    def setnum(self):
        print("숫자를 정하는 중입니다 ",end="") #바로 옆에 이어서 출력시키기
        for i in range(15):     # > 기호 15개 출력
            print(end="> ")
            self.loding()   #로딩되는 것처럼 보이기
        print("숫자를 정하였습니다.")
    
    #로딩되는 것처럼 보임
    def loding(self):
        time.sleep(0.2)

    #최종 결과
    def end(self):
        print("\n< < < 최종결과  > > >")
        if self.total >= 5:
            print("Congratulations on your success!!")
            print("축하합니다!! 총 "+str(self.total)+"점으로 성공하셨습니다!!") 
        else:
            print("I am afraid you failed.")
            print("아쉽게도 총 "+str(self.total)+"점으로 5점보다 낮으므로 실패하셨습니다.")
