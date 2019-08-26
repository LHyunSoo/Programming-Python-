from coffee import Coffee
from bubbleTea import BubbleTea

class Order:

    def __init__(self):
        self.order_menu = []

    def show_menu(self):
        print("0: 아메리카노 1800원, 1: 하동녹차오레오 3900원")
    
    def order_drink(self):

        while True:
            #show menu
            self.show_menu()

            #주문받기, 음료선택하기
            order = input("무엇을 고르시겠습니까? ")
            if order == "":
                break
            if int(order) == 0:
                drink = coffee("아메리카노",1800)
            elif int(order) == 1:
                _drinks = bubbleTea("하동녹차오레오", 3900)

            #음료 옵션선택하기
            drink.order()

            self.order_menu.append(drink)
        
        #주문한 음료 내용 보여주기
        for d in self.order_menu:
            print(d)

        #합계 금액 보여주기
        print("총금액: "+str(self.sum_price())+"원")
        
    def sum_price(self):
        sum = 0
        for d in self.order_menu:
            sum += d.price

        return sum
