class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result = []
        sum = 0

        nums.sort()
        # print(nums) 

        # list 원소 2개씩 묶어서 2차원 리스트 만들기
        for i in range(0, len(nums), 2): # 0 ~ 전체요소의 갯수까지 2 step씩 반환
            result.append(nums[i:i+2]) # nums[i:i+2] => i번째 인덱스 ~ i+2번째 인덱스 앞까지 가지고 옴
        # print(result) # [[1, 2], [3, 4]]

        for i in result:
            # print(i)
            sum += min(i)
        
        # print(sum)
        return sum