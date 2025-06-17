class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children : 
            return -1
        money = money - children
        res = 0
        while money > 6 and res < children-1:
            money -= 7
            res += 1
        if money == 3 and res == children - 1:
            return res - 1
        if money == 7:
            res += 1
        return res
        
        
        
            
        
