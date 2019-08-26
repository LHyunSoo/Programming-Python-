for item in {"HTML5","CSS3","JavaScript"}:
    print(item+"를 할 수 있다.")
#리스트 안에 리스트
table = [
    ["월","화","수"],
    [1,2,3]
]
for row in table:
    for col in row:
        print(col)
    print("----")