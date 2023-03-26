# https://wikidocs.net/22

# for in list : 파이썬 반복문 => 순회할 list가 정해져 있을 때 사용
# for in range(시작숫자, 종료숫자, step) : 연속된 정수를 만드는 함수 / 시작숫자와 step 생략 가능 => 순회할 횟수가 정해져 있을 때 사용
# len(s) : 입력값 s의 길이를 리턴하는 함수

class Solution1:
    def twoSum(self, nums, target):
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): # i+1을 하지 않으면 자기 자신과 덧셈이 이루어져 예외처리 필요
                # print(i, nums[i], j, nums[j])
                if nums[i] + nums[j] == target:
                    # print (i, j)
                    return [i, j]


Solution1().twoSum(nums = [2,7,11,15], target = 9) # [0,1]
# Solution1().twoSum(nums = [3,2,4], target = 6) # [1,2]
# Solution1().twoSum(nums = [3,3], target = 6) # [0,1]


# 시간복잡도 : O(n2) => 🚨 제약조건 상 time out 나올 가능성이 있음!!
# 이중반복문


# 시간복잡도 : O(nlonn) 풀이 방법
class Solution2:
    def twoSum(self, nums, target):

        left, right = 0, len(nums) -1 # left, right 할당

        while( left != right ):
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
            	return [left, right]

        
## 투포인터 방식으로는 풀 수 없음, 정렬을 하게 되면 인덱스가 꼬이기 때문에!

Solution2().twoSum(nums = [2,7,11,15], target = 9) # [0,1]
Solution2().twoSum(nums = [3,2,4], target = 6) # [1,2]
Solution2().twoSum(nums = [3,3], target = 6) # [0,1]
