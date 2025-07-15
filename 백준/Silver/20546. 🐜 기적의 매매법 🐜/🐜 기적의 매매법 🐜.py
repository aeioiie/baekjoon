money = int(input())
stock_prices = list(map(int, input().split()))

# JH
JH_buy = 0
JH_money = money
for i in range(len(stock_prices)):
    JH_buy_now = JH_money // stock_prices[i]
    JH_buy += JH_buy_now
    JH_money -= JH_buy_now * stock_prices[i]

JH_asset = JH_buy * stock_prices[-1] + JH_money

# SM    
SM_buy = 0
SM_money = money
for i in range(len(stock_prices)):
    if i >= 3:
        if stock_prices[i-3] < stock_prices[i-2] and stock_prices[i-2] < stock_prices[i-1] and stock_prices[i-1] < stock_prices[i]: # i+1번째 날에는 주식이 하락할 것 -> 전량 매도
            SM_money += stock_prices[i] * SM_buy
            SM_buy = 0
        elif stock_prices[i-3] > stock_prices[i-2] and stock_prices[i-2] > stock_prices[i-1] and stock_prices[i-1] > stock_prices[i]: # i+1번째 날에는 주식이 상승할 것 -> 전량 매수
            SM_buy_now = SM_money // stock_prices[i]
            SM_buy += SM_buy_now
            SM_money -= SM_buy_now * stock_prices[i]
            # 예를들어서 현재 현금이 20, 주가가 33, 보유 주식 수가 2라면
            # 전량 매도 시 현금은 20 + 33 x 2 = 86, 보유 주식 수는 0
            # 주가 x 보유 주식 수 + 현금

SM_asset = SM_buy * stock_prices[-1] + SM_money

if JH_asset > SM_asset:
    print("BNP")
elif JH_asset < SM_asset:
    print("TIMING")
else:
    print("SAMESAME")

# print(JH_asset, SM_asset)