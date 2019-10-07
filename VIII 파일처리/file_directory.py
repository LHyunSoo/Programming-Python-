import os
data = os.listdir("c:/") #"."은 현재 디렉토리 ".."은 상위 디렉토리
                          # ""안에 있는 \ 는 특수하게 \n 같이 쓰이는 경우가 있어서 \\ 두번 써줘야지 인식함
print(data)
for d in data :
    print(d)
    print("is directory? : " + str(os.path.isdir(d)))
    print("is file? : ", str(os.path.isfile(d)))