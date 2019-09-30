#p239
class OddError(Exception):
    def __init__(self, message="홀수는 ㄴㄴ"):
        self.message=message

    def __str__(self):
        return self.message

n=11
try:
    if n % 2 != 0:
        raise OddError      #에러 발생
    else:
        print("짝수입니다.")
except OddError as e:       #에러 처리
    print(e)