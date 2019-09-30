fi=open("test.ama","w",encoding="utf-8")
fi.write("아이스아메리카노\t2800\t레귤러\t100%\t50%\t코코\n")
fi.write("오레오쉐이크\t3500\t레귤러\t50%\t150%\t타피오카\n")
fi.write("하동녹차오레오\t4200\t점보\t50%\t200%\t타피오카\n")
fi.close()

fi=open("test.ama","r",encoding="utf-8")
sum=0
while True:
    data = fi.readline()
    if not data:
        break
    l = data.split()    # 화이트스페이스(띄어쓰기, \t, \n 등)로 분리
    print(l[1]+"원")
    sum+=int(l[1])
print("합계 : "+str(sum)+"원")
fi.close()