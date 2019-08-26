# 학번을 입력받고,
# 학년 학과 반 번호를 출력하자
# 예)
#   학번을 입력하시오. : 2520
#   2학년 뉴미디어디자인과 5반 20번입니다.
#   3학년도 되게 하려면?

num = input("학번을 입력하시오. : ")

if num[0] == '3':
    if num[1] == '1' or num[1] == '2':
        major = "인터랙티브미디어과" 
    elif num[1] == '3' or num[1] == '4':
        major = "뉴미디어디자인과"
    elif num[1] == '5' or num[1] == '6':
        major = "뉴미디어솔루션과"
else :
    if num[1] == '1' or num[1] == '2':
        major = "뉴미디어소프트웨어과"
    elif num[1] == '3' or num[1] == '4':
        major = "뉴미디어웹솔루션과"
    elif num[1] == '5' or num[1] == '6':
        major = "뉴미디어디자인과"

print(num[0]+"학년 "+major+" "+num[1]+"반 "+num[2:4]+"입니다.")