res_trades= [120 , 80 , -95 , -100 , -3.5 , -45 , -35 , 65 , 150 , 100 , -25 , -20 , 15 ,76 , 70 , 50 , 44 , 35 , 120 , 85 , -50]

win_trade = 0

for i in res_trades:
    if i > 0 :
        win_trade += 1


all_trade = len(res_trades)


loss_trade = all_trade - win_trade


win_rate = (win_trade*100)/all_trade

net_profit= 0
for i in res_trades:
    net_profit += i
    

max_consecutive_loss = 0
max_consecutive_win = 0
counter_win = 0
counter_loss = 0

for i in res_trades:
    if i > 0 :
        counter_loss = 0
        counter_win += 1
        if max_consecutive_win <= counter_win :
            max_consecutive_win = counter_win
    else:
        counter_win = 0
        counter_loss += 1 
        if max_consecutive_loss <= counter_loss:
            max_consecutive_loss = counter_loss



print("number of all trade :",all_trade)
print("number of win trade :",win_trade)
print("number of loss trade :",loss_trade)
print("win rate is :",round(win_rate,2),"%")
print("net profit is :",net_profit)
print("max consecutive win :",max_consecutive_win)
print("max consecutive loss :",max_consecutive_loss)





















        