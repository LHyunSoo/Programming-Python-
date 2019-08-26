#학번 입력받아
#학과 추력하기
#예 : "2315"를 입력하면, "뉴미디어웹솔루션과"를 출력

# st12 = ["뉴미디어소프트웨어과","뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어웹솔루션과","뉴미디어디자인과","뉴미디어디자인과"]
# st3 = ["인터랙티브미디어과","인터랙티브미디어과","뉴미디어디자인과","뉴미디어디자인과","뉴미디어솔루션과","뉴미디어솔루션과"]

majors = [
    ["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
    ["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
    ["인터랙티브미디어과","뉴미디어디자인과","뉴미디어솔루션과"]
]

for i in range(3):
    num = input("학번을 입력하시오. : ")

    # if num[0] == '1' or num[0] == '2' :
    #     if num[1] == '1' or num[1] == '2' :
    #         print("뉴미디어소프트웨어과")
    #     elif num[1] == '3' or num[1] == '4' :
    #         print("뉴미디어웹솔루션과")
    #     elif num[1] == '5' or num[1] == '6' :
    #         print("뉴미디어디자인과")
    #     else :
    #         print("존재하지 않음")
    # elif num[0] ==  '3' :
    #     if num[1] == '1' or num[1] == '2' :
    #         print("인터랙티브미디어과")
    #     elif num[1] == '3' or num[1] == '4' :
    #         print("뉴미디어디자인과")
    #     elif num[1] == '5' or num[1] == '6' :
    #         print("뉴미디어솔루션과")
    #     else :
    #         print("존재하지 않음")
    # else :
    #     print("오류")

    grade = num[0]
    grade = int(grade)
    classroom = num[1]
    classroom = int(classroom)

    # if grade == 1 or grade ==2:
    #     print(st12[(classroom - 1)//2])
    # elif grade == 3:
    #     print(st3[(classroom - 1)//2])

    print(majors[grade-1][(classroom - 1)//2])