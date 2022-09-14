def findmaxprofit(price):
 
    n = len(price)
    if n == 0:
        return 0
 
    profit = [0] * n
 
    profit[n - 1] = 0

    max__so__far = price[n - 1]

    for i in reversed(range(n - 1)):
        profit[i] = max(profit[i + 1], max_so_far - price[i])
        max_so_far = max(max_so_far, price[i])
    min_so_far = price[0]
    for i in range(1, n):
        profit[i] = max(profit[i - 1], (price[i] - min_so_far) + profit[i])
        min_so_far = min(min_so_far, price[i])
    return profit[n - 1]
 
 
if __name__ == '__mai__':
 
    price = [7,1,5,3,6,4]
 
    print('The maximum profit is',findmaxprofit(price))
     
