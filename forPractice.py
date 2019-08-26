for x in range(3,9,2):
    print(x)

print("=========================")

for ch in "LOVE":
    print(ch)

print("=========================")

for item in ["힙합","발라드"]:
    print(item+"를(을) 즐겨듣는다.")

print("=========================")

for item in (2560,1440):
    print(item)

print("=========================")

pl  = {"C":1972,"JAVA":1995,"Python":1991}
for key in pl :
    print(": 일때 >> ",key, ":", pl[key])
    print("+ 일때 >> "+key+":"+str(pl[key]))
    print("-------------------")

print("=========================")

for key, value in pl.items():
    print(key, " : ", value)

print("=========================")

for itme in {"HTML5", "CSS3", "JavaScript"}:
    print(item+"를 할 수 있다.")