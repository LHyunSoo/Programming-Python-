from datetime import datetime

# 내가 태어난 날은 무슨 요일일까?
birthday=datetime(2002,1,1,13,0,0)
birthweekday=birthday.weekday()
if birthweekday == 0:
    birthweekday='월요일'
elif birthweekday == 1:
    birthweekday='화요일'
elif birthweekday == 2:
    birthweekday='수요일'
elif birthweekday == 3:
    birthweekday='목요일'
elif birthweekday == 4:
    birthweekday='금요일'
elif birthweekday == 5:
    birthweekday='토요일'
else:
    birthweekday='일요일'
print('내가 태어난 날은 ',birthweekday,'입니다.')
print()

# 나는 며칠 살았을까?
today = datetime.now()
print('나는 ',today - birthday,'살아왔다.')
print()

# 올해 크리스마스 며칠 남았을까?
christmas=datetime(2019,12,25,0,0,0)
print('올해 크리스마스는 ',christmas - today,'남았다.')
print()