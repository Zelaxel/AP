from sys import maxsize as infinite

def solve(coins, change):
    
    sorted_coins = coins.copy()
    sorted_coins.sort(reverse=True)
    taken = []
    
    total = 0
    for coin in sorted_coins:
        
        index = None
        for i in range(len(coins)):
            if coins[i] == coin and (i + 1) not in taken:
                index = i
        
        if total + coin <= change:
            total += coin
            taken.append(index + 1)
            
        if total == change:
            taken.sort()
            return taken
            
    return None
