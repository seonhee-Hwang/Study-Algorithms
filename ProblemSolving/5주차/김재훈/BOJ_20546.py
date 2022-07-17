# 준현이와 성민이의 세기의 주식 대결 (개미 코인)
start_money = int(input())

prices = [*map(int, input().split())]

class Person():
    def __init__(self, _money):
        self.money = _money
        self.stock = 0
        self.total_money = _money

    def update(self, _price):
        self.total_money = self.money + self.stock * _price


JH = Person(start_money)
SM = Person(start_money)

up_strike = 0
down_strike = 0
for i, price in enumerate(prices):
    if (JH.money // price) != 0:
        tmp = JH.money // price
        JH.stock += tmp
        JH.money -= tmp * price
        # 기도한다.

    if i == 0:
        pass
    else:
        if prices[i - 1] < price: # 어제보다 오른 상태
            up_strike += 1
            down_strike = 0
        elif prices[i - 1] > price: # 어제보다 내린 상태
            up_strike = 0
            down_strike += 1
        elif prices[i - 1] == price:
            up_strike = 0
            down_strike = 0
        else:
            print("???? 이상함")
    
    if down_strike >= 3:
        tmp = SM.money // price
        SM.money -= price * tmp
        SM.stock += tmp

    if up_strike >= 3:
        SM.money += price * SM.stock
        SM.stock = 0

    JH.update(price)
    SM.update(price)
    # print(f'JH {JH.total_money}, SM {SM.total_money}')

# SM_Total = SM.money + SM.stock * prices[-1]
# JH_Total = JH.money + JH.stock * prices[-1]

if SM.total_money > JH.total_money:
    print("TIMING")
elif SM.total_money < JH.total_money:
    print("BNP")
else:
    print("SAMESAME")
