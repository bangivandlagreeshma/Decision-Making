'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00

'''

def determine_profit_or_loss(totalCost, sp_per_banana):
    cost_per_banana = totalCost / 12
    total_sp = sp_per_banana * 12

    profit_or_loss = total_sp - totalCost

    if profit_or_loss > 0:
        return f"Profit : Rs.{profit_or_loss:.2f}"
    elif profit_or_loss < 0:
        return f"Loss : Rs.{-profit_or_loss:.2f}"
    else:
        return "No Profit No Loss"
totalCost = float(input())
sp_per_banana = float(input())
result = determine_profit_or_loss(totalCost, sp_per_banana)
print(result)
