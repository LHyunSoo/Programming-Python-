fi = open("text.ama", "w", encoding = "utf-8")
fi.write("아이스아메리카노\t2800\t레귤러\t100%\t50%\t코코\n")
fi.write("오레오쉐이크\t3500\t점보\t50%\t150%\t타피오카\n")
fi.write("딸기코코넛\t3500\t점보\t0%\t150%\t알로에\n")
fi.close()

fi = open("text.ama", "r", encoding = "utf-8")

sum=0
while True :
    data = fi.readline()
    if not data :
        break #읽어오는 데이터 값이 없으면 멈춰라
    l = data.split() #괄호에 자르는 단위를 안 적어주면 화이트스페이스로 분리
                     #화이트스페이스(띄어쓰기, \t, \n 등)으로 분리
    print(l[1]+"원")
    sum += int(l[1])
fi.close()
print("주문한 총금액 : " + str(sum) + "원")