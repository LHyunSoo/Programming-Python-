f = open("file.txt", "w", encoding = "utf8") #w는 덮어쓰기 a는 붙여쓰기

f.write("반갑다")
f.write("\n")
f.write("세상아")

f.close()