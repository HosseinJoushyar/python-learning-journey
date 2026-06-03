first_acount= [120 , 80 , -95 , -115 , -30 , -45 , -35 , 65 , 190 , 100 , -25 , -20 , 15 ,76 , 70 , 50 , 44 , 35 , 120 , 89 , 85 , -50]
second_acount= [90, 100, -80, 30 , -24 , -40 , -50 , -45 , -90 , -25 - -85 , 40 , 50 ,30 , 40 , 90 , 180 , 45 , 75 , 30 , -120 , -90 , 35 , 88 , 20 , -74]



def total_trade(trades):
    return len(trades)



def win_trade(trades):
    win_trade = 0
    for i in trades:
        if i > 0 :
            win_trade += 1
    return win_trade




def loss_trade(trades):
    res = total_trade(trades)- win_trade(trades)
    return res



def winrate (trades):
    rate = ((win_trade(trades)*100)/total_trade(trades))
    return  rate





def net_profit(trades):
    return sum(trades)



def best_profit(trades):
    return max(trades)

    

def worst_loss(trades):
    return min(trades)

    

def consecutive_win(trades):
    
    max_consecutive_win = 0
    counter_win = 0
    
    for i in trades:
    
        if i > 0 :
            counter_win += 1
            if counter_win > max_consecutive_win :
                max_consecutive_win = counter_win
        else:
            counter_win = 0
    return max_consecutive_win
                
                
def consecutive_loss(trades):
    
    max_consecutive_loss = 0
    counter_loss = 0
    
    for i in trades :
        if i <= 0:
            counter_loss += 1 
            if counter_loss > max_consecutive_loss :
                max_consecutive_loss = counter_loss
        else:
            counter_loss = 0
                
    return max_consecutive_loss 

def average_loss(trades):
    loss_count = len(list(filter(lambda x: x<0 , trades)))
    sum_loss = sum(filter(lambda x: x<0 , trades))
    return sum_loss/loss_count

def average_win (trades):
    win_count = len(list(filter(lambda x: x>0 , trades)))
    sum_win = sum(filter(lambda x: x>0 , trades))
    return sum_win/win_count

def risk_to_reward (trades):
    return abs((average_win(trades)/average_loss(trades)))

def profit_factor(trades):
    sum_win = sum(filter(lambda x: x>0, trades))
    sum_loss = sum(filter(lambda x: x<0, trades))
    return abs(sum_win/sum_loss)

def print_report(trades):
    print("\n\n")
    print("===== Trading Report =====\n")
    print("number of total trade :",total_trade(trades))
    print("number of win trade :",win_trade(trades))
    print("number of loss trade :",loss_trade(trades))
    print("win rate is :",round(winrate(trades),2),"%\n")
    print("net profit is :",net_profit(trades), "\n")
    print("max consecutive win :",consecutive_win(trades))
    print("max consecutive loss :",consecutive_loss(trades) , "\n")
    print("best profit is :",best_profit(trades))
    print("worst loss is :",worst_loss(trades) , "\n")
    print("average loss :",round(average_loss(trades),2))
    print("average win :",round(average_win(trades),2) , "\n")
    print("RR :",round(risk_to_reward(trades),1))
    print("profit factor :",round(profit_factor(trades),1) , "\n")
    print("=======================================")
    
print_report(first_acount)
print_report(second_acount)























        