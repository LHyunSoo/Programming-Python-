# p.107~
import random

def rolling_dice():
    n = random.randint(1,6) #1~6
    print("여섯면 주사위 굴린 결과 : ",n)

def rolling_dice(pip):  
    n = random.randint(1,pip)
    print(pip,"면 주사위 굴린 결과 : ",n)

def rolling_dice(pip, repeat):  # 오버로딩이 안됌. 위에 rolling_dice()함수들은 없어짐
    for r in range(1,repeat+1):
        n = random.randint(1,pip)
        print(pip,"면 주사위 굴린 결과",r," : ",n)

rolling_dice(6,2)
rolling_dice(8,-2)
rolling_dice(20,0)

#------------------------------------------------------------------------------------------------------------------------------------------------------

def star():
    print("*****")

star()
star()
star()

print("♡")
print("♡","♪")
print("♡","♪","♧")
print("♡","♪","♧","♠")
print("♡","♪","♧","♠","★")

def p(*args):
    str = ""
    for a in args:
        str+=a
    print(str)

def p(space, space_num,*args):
    string = args[0]
    for i in range(1,len(args)):
        string += (space * space_num)+args[i]
    print(string)

p(",",3,"♡")
p("♡",2,"♪")
p("♠",4,"_","냥","♧")

def star2(ch,*nums):
    for i in range(len(nums)):
        print(ch * nums[i])
    # for n in nums:
    #     print(ch*n)

star2("♬",3)
star2("♡",1,2,3)

def fn(a,b,c,d,e):
    print(a,b,c,d,e)

fn(1,2,3,4,5)
fn(10,20,30,40,50)
fn(5,6,7,8,9)
fn(a=1,b=2,c=3,d=4,e=5)
fn(e=5,d=4,c=3,b=2,a=1)
fn(1,2,c=3, e=5,d=4)
#fn(d=4,e=5,1,2,3)   #Error

star("*",3,"_",2,3)
def star(mark,repeat,space,space_repeat, line):
    for _ in range(line):
        string += (mark * repeat) + (space * space_repeat) + (mark * repeat)
        print(string)

def hello(msg="안녕"):
    print(msg + "!")

hello("하이")
hello("니하오")
hello("곤니찌와")
hello()

def fn(a,b=[]):
    b.append(a)
    print(b)

fn(3)       #[3]
fn(5)       #[3, 5]
fn(10)      #[3, 5, 10]
fn(7,[1])   #[1, 7]
#fn(a=7, b=[1]):    b를 대체하는 순간 원래 b는 덮어 씌워진다.
#   print([1].append(7))

#------------------------------------------------------------------------------------------------------------------------------------------------------

def gugudan(dan=2):
    print("<<",dan,"단 >>")
    for j in range(1,9+1):
        print(dan,"X",j,"=",dan*j)
    print()

gugudan(3)
gugudan(2)
gugudan()

#------------------------------------------------------------------------------------------------------------------------------------------------------

def sum(*numbers):
    sum_value = 0
    for number in numbers:
        sum_value +=number

    return sum_value

print("1 + 3 =",sum(1,3))
print("1 + 3 + 5 + 7 =",sum(1,3,5,7))

def min(*numbers):
    min_value = numbers[0]
    for number in numbers:
        if min_value > number:
            min_value = number
    return min_value

print("min(3, 6, -2) =",min(3,6,-2))

def max(*numbers):
    max_value = numbers[0]
    for number in numbers:
        if max_value < number:
            max_value = number
    return max_value

print("max(8, 1, -1, 12) =",max(8, 1, -1, 12))

def multi_num(multi,start,end):
    result = []
    for n in range(start,end):
        if n % multi==0:
            result.append(n)
    return result

print("multi_num(17, 1, 200) =",multi_num(17, 1, 200))
print("multi_num(2, 3, 100) =",multi_num(2, 3, 100))

def min_max(*args):
    min_value = args[0]
    max_value = args[0]
    for a in args:
        if min_value > a:
            min_value = a
        if max_value < a:
            max_value = a
    return min_value, max_value

min,max = min_max(52, -3, -29, 2, 0)
print("최솟값:",min, "최댓값:",max)