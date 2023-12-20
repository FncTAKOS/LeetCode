class Solution(object):
    def buyChoco(self, prices, money):
        smallest=min(prices)
        prices.remove(smallest)
        smallest2=min(prices)
        sum=money-(smallest+smallest2)
        return sum if sum>=0 else money