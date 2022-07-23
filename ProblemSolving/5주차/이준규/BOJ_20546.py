money = int(input())
stock_price = list(map(int, input().split()))
# print(stock_price)
# 1. BNP
J_money = money
J_cnt = 0
for i in range(len(stock_price)):
    today = stock_price[i]
    if J_money < 0:
        continue
    if J_money >= today:
        J_cnt = J_money // today
        # print(J_cnt)
        J_money -= J_cnt*today
        # if J_money // stock_price[i] > 0:
        #     J_money -= stock_price[i] * (J_money // stock_price[i])
        #     J_cnt += J_money // stock_price[i]
        #     print(J_cnt)
J_money += J_cnt * stock_price[-1]
# print(J_money)

# 2. TIMING
S_money = money
S_cnt = 0
rise_cnt = 0
fall_cnt = 0
tmp_price = 0
for j in range(len(stock_price)):
    # 현재 주식가
    if j == 0:
        tmp_price = stock_price[j]
    if stock_price[j] > tmp_price:
        tmp_price = stock_price[j]
        rise_cnt += 1
        fall_cnt = 0
    elif stock_price == tmp_price:
        rise_cnt = 0
        fall_cnt = 0
    else:
        tmp_price = stock_price[j]
        rise_cnt = 0
        fall_cnt += 1

    if fall_cnt >= 3:
        if S_money // stock_price[j] > 0:
            S_cnt += S_money // stock_price[j]
            S_money -= stock_price[j] * (S_money // stock_price[j])

    elif rise_cnt >= 3:
        S_money += S_cnt * stock_price[j]
        S_cnt = 0

S_money += S_cnt * stock_price[-1]

print(J_money)
print(S_money)
if J_money > S_money:
    print("BNP")
elif J_money < S_money:
    print("TIMING")
else:
    print("SAMESAME")
