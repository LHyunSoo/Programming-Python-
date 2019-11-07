#2315 이현수
#자신의 얼굴형에 맞는 헤어스타일을 추천해주는 프로그램입니다.
#hairstyle.py 실행하면 됩니당

import sys

class HairStyle:

    # 실행할 함수 (첫 화면)
    def start(self):
        print("----- [ 모(毛)두(頭)의 헤어 ] --------------------------------------------------------------------------------------")
        print("1) 헤어스타일 추천받기")
        print("2) 기록 확인하기")
        print("3) 프로그램 사용법")
        ch = input("> > > ")

        if ch == "1":   #헤어스타일 추천받기
            self.info()
        elif ch == "2":     #기록 확인하기
            self.fileread()
        elif ch == "3":     #프로그램 사용법
            self.help()


    # 도움말
    def help(self):
        print("====================================================================================================================")
        print("< 모두의 헤어 사용법 >")
        print("1. \"헤어스타일 추천받기\"를 선택하세요.")
        print("2. 이름과 성별을 입력하세요.")
        print("3. 추천받고 싶은 방법을 선택하세요.")
        print("4. \"얼굴형별 헤어스타일\"을 선택한 경우")
        print("\t(1) 자신의 얼굴형을 선택하세요. ")
        print("\t(2) 자신의 얼굴형에 어울리는 헤어스타일을 알려줍니다.")
        print("5. \"얼굴길이별 헤어스타일\"을 선택한 경우")
        print("\t(1) 귀 밑부터 턱 끝까지 길이를 입력하세요.")
        print("\t(2) 단발이 어울리는지 장발이 어울리는지 알려줍니다.")
        self.start()    #다시 처음으로 돌아가기


    # 정보 입력
    def info(self):
        print("====================================================================================================================")
        print("< 이름을 입력하세요! >")
        name=input("이름 : ")
        self.filewrite(name)

        print("< 성별을 입력하세요! >")
        print("남자는 얼굴형별 헤어스타일만 추천해줍니다.")
        gender = input("성별(여자: 1, 남자: 2) : ")

        if gender == "1":   #여자
            self.filewrite(1)
            self.recomWay(gender)     #추천해줄 방법 선택하는 화면으로
        elif gender == "2": #남자
            self.filewrite(2)
            self.faceShape(gender)    #얼굴형 선택하는 화면으로


    def recomWay(self,g):     #추천해줄 방법 선택하는 화면
        print("====================================================================================================================")
        print("< 추천 방법을 선택하세요! >")
        print("1) 얼굴형별 헤어스타일")
        print("2) 얼굴길이별 헤어스타일")
        way=input("> > > ")

        if way == "1":  #얼굴형별 헤어스타일
            self.filewrite(1)
            self.faceShape(g)
        elif way == "2":    #얼굴길이별 헤어스타일
            self.filewrite(2)
            self.length()


    def faceShape(self,g):    #얼굴형 선택하는 화면
        print("====================================================================================================================")
        print("< 얼굴형을 선택하세요! >")
        print("1) 긴형")
        print("2) 둥근형")
        print("3) 역삼각형")
        print("4) 각진(네모)형")
        shape=input("> > > ")

        if shape == "1":    #긴형
            self.endfilewrite(1)
            self.long(g)
        elif shape == "2":  #둥근형
            self.endfilewrite(2)
            self.circle(g)
        elif shape == "3":  #역삼각형
            self.endfilewrite(3)
            self.triangle(g)
        elif shape == "4":  #각진(네모)형
            self.endfilewrite(4)
            self.square(g)


    # 얼굴형별 헤어스타일 추천
    def long(self,g):     #긴 얼굴형 헤어스타일 추천
        print("====================================================================================================================")
        print("< 긴형 >")

        if g == "1":  # 여자
            print("- 볼륨감 있는 반 곱슬 느낌의 스타일이나 꽉찬 뱅 앞머리나 시스루 뱅으로 시선을 분산시키나 옆머리에 볼륨을 넣는 스타일")
            print("- 가르마: 8:2")
            print("* 피해야 할 스타일 : 촥 달라 붙는 생머리")
        elif g == "2":  # 남자
            print("- 앞머리를 살짝 내려 이마를 답답하지 않게 자연스럽게 가리는 스타일")

    def circle(self,g):   #둥근얼굴형 헤어스타일 추천
        print("====================================================================================================================")
        print("< 둥근형 >")

        if g=="1":  #여자
            print("- 시각적으로 갸름하게 보여주는 레이어드 C컬펌, 뿌리볼륨펌, 턱선까지 오거나 미디엄보다 긴 기장")
            print("- 가르마: 5:5 (세련되고 시크한 이미지를 부각)")
            print("* 피해야 할 스타일 : 미디엄 길이, 곱슬머리(파마)")
        elif g == "2":  # 남자
            print("- 정수리 볼륨을 살리고 이마를 드러내는 스타일")

    def triangle(self,g): #역삼각형 헤어스타일 추천
        print("====================================================================================================================")
        print("< 역삼각형 >")

        if g == "1":  # 여자
            print("- C컬펌 또는 무거운 느낌의 굵은 S컬펌과 머리를 한쪽으로 넘겨 웨이브를 준 스타일")
            print("- 가르마: 1:9 (섹시하고 도회적인 이미지를 부각)")
            print("* 피해야 할 스타일 : 답답해 보이는 앞머리")
        elif g == "2":  # 남자
            print("- 구렛나룻을 자연스럽게 살리며 너무 짧지 않고 자연스러운 스타일")

    def square(self,g):   #각진(네모)형 헤어스타일 추천
        print("====================================================================================================================")
        print("< 각진(네모)형 >")

        if g == "1":  # 여자
            print("- 단발 굵은 S컬펌, 미디엄 길이 레이어드 C컬펌, 애교머리에 자연스럽게 웨이브를 준 스타일")
            print("- 가르마: 7:3 이나 8:2 (청순하고 선한 이미지를 부각)")
            print("* 피해야 할 스타일 : 5:5 정가르마, 반듯한 일자 앞머리")
        elif g == "2":  # 남자
            print("- 적당한 길이의 가벼운 컬로 얼굴 윤곽을 부드럽게 표현")


    # 얼굴길이별 헤어스타일
    def length(self):
        print("====================================================================================================================")
        print("< 길이를 입력해주세요! >")
        l=float(input("귀 밑부터 턱 끝까지 길이(단위 : cm) : "))
        self.filewrite(l)
        self.lengResult(l)

    # 단발이 어울릴지 아닐지 판별하는 함수
    def lengResult(self,l):
        criteria = 5.715

        if l<=criteria:    #단발이 어울림
            self.endfilewrite("단발")
            self.goshort()
        else:   #장발이 어울림
            self.endfilewrite("장발")
            self.noshort()

    # 단발이 어울린다고 알려주는 함수
    def goshort(self):
        print("====================================================================================================================")
        print(" ╭╮___╭╮")
        print("( ⊙□⊙) 어머! 단발이 찰떡이실 것 같군요!!")
        print("/つ 지금 당장 단발하러 미용실 ㄱㄱ!!")

    # 단발이 어울리지 않는다고 알려주는 함수
    def noshort(self):
        print("====================================================================================================================")
        print(" ╭╮_╭╮")
        print("( ･ェ･) 혹시 단발병에 걸린 상태라면")
        print("/つ 검색창에 \"단발병 퇴치\"를 쳐보세요..")


    # 파일 입력 구현
    def filewrite(self, num):
        try:
            with open("faceshape.txt", mode='a', encoding='utf-8') as f:
                f.write(str(num) + " ")
        except:
            print("Error: 파일쓰기 에러 발생")
            sys.exit(1)

    def endfilewrite(self, num):
        try:
            with open("faceshape.txt", mode='a', encoding='utf-8') as f:
                f.write(str(num) + "\n")
        except:
            print("Error: 파일쓰기 에러 발생")
            sys.exit(1)

    #파일 출력 구현
    def fileread(self):
        r = True
        while(r):
            try:
                print("====================================================================================================================")
                print("< 기록 >")
                with open("faceshape.txt", mode='r', encoding='utf-8') as f:
                    while(True):
                        data = f.readline().split()
                        name = data[0]
                        gender = data[1]
                        select1 = data[2]

                        print("이름: " + name, end=' ')
                        if gender == "1":
                            select2 = data[3]
                            if select1 == "1":
                                if select2 == "1":
                                    print(" / 성별: 여자 / 얼굴형: 긴형")
                                elif select2 == "2":
                                    print(" / 성별: 여자 / 얼굴형: 둥근형")
                                elif select2 == "3":
                                    print(" / 성별: 여자 / 얼굴형: 역삼각형")
                                elif select2 == "4":
                                    print(" / 성별: 여자 / 얼굴형: 각진(네모)형")
                            elif select1 == "2":
                                select3 = data[4]
                                print(" / 성별: 여자 / 길이: " + select2+" / 어울리는 머리길이: "+select3)
                        elif gender == "2":
                            if select1 == "1":
                                print(" / 성별: 남자 / 얼굴형: 긴형")
                            elif select1 == "2":
                                print(" / 성별: 남자 / 얼굴형: 둥근형")
                            elif select1 == "3":
                                print(" / 성별: 남자 / 얼굴형: 역삼각형")
                            elif select1 == "4":
                                print(" / 성별:남자 / 얼굴형: 각진(네모)형")

            except Exception as e:
                pass

            print("====================================================================================================================")
            re = input("메인으로 돌아가시겠습니까?(y/n): ")
            if re == "y" or re == "Y":
                hs.start()
            elif re == "n" or re == "N":
                r=False
                

hs = HairStyle()
hs.start()
hs.fileread()