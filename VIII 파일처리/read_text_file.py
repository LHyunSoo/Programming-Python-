f = open("file.txt", "r")  #r : read text

text = f.read()
print(text)

f.close()

#한줄씩 읽어오자
f = open("file.txt", "r", encoding = "utf-8")

text0 = f.readline()
print(text0)
text1 = f.readline()
print(text1)
text2 = f.readline
print(text2)

f.close()
