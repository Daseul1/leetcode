# 1. prices list의 최솟값 찾기
# 2. 최소값의 인덱스 ~ 끝까지 list slice
# 3. slice 된 list의 최댓값 찾기(없다면 0)
# 4. 최대값의 값이 존재한다면 최솟값과 차 구하기, 없다면 0

# 실패
# list의 최솟값만 생각하다가,[2,4,1] 과 같은 패턴을 생각하지 못함 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        small = prices.index(min(prices)) # 최소값의 인덱스 찾기

        # 최소값의 인덱스 ~ 끝까지 slice
        slicePrices = prices[small:]
        # print(slicePrices)
       
       # slice 된 배열의 최댓값 구하기 / 없다면 0
        if len(slicePrices) == 0:
            big = 0
        else:
            big = max(slicePrices)
        print(big)

        # 최댓값 - 최솟값
        if big != 0:
            result = big - min(prices)
        else:
            result = 0
        return result    




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 # 이익 할당
        min_price = max(prices) # 최솟값을 최대값으로 할당하여 비교하여 최솟값 계속 갱신해 줄것

        # 최솟값과 profit 구하기
        for price in prices:
            min_price = min(min_price, price)
            # print(min_price, price, profit, price - min_price)
            profit = max(profit, price - min_price)
        return profit