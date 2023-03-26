class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        # 반복문 : i가 최댓값일 때 left, right 가 존재하기 위해서 범위를 -2까지 지정
        for i in range(len(nums) - 2):
            # 중복 제거를 위해 같은 수는 넘어가기
            if i > 0 and nums[i] == nums[i - 1]:
                continue # 아래 코드들 실행되지 않고 건너뜀

            # 중복이 아닌 경우 투포인터 풀이
            # left, right -> i + 1(i의 다음 지점), 배열 맨 마지막 값(i의 마지막 지점)으로 지정 (간격을 좁혀 가는 이동을 할 것이기에)
            left, right = i + 1, len(nums) - 1

            # 간격을 좁혀가면 더하기
            while left < right: # 오름차순으로 정렬하였으므로, left값이 right 값보다 작을때까지로 조건 지정
                sum = nums[i] + nums[left] + nums[right]
                # 3개 인자의 합이 0보다 작으면, 값을 더 키워야하므로 left를 우측으로 이동
                #                   크면, 값을 줄여야하므로 right를 좌측으로 이동
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0 이면, 리스트 변수 result에 추가
                    result.append([nums[i], nums[left], nums[right]])

                    # left, right 양 옆으로 동일한 값이 있으면 스킵 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 마지막으로 left를 우측으로 한 칸, right를 좌측으로 한 칸 이동하여 위 로직 반복
                    left += 1
                    right -= 1

         # result 리턴      
        return result


# 실패
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        temp = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for l in range(i+2, len(nums)):
                    if nums[i] + nums[j] + nums[l] == 0:
                        # print(nums[i], nums[j], nums[l])
                        aaa = [nums[i], nums[j], nums[l]]
                        aaa.sort()
                        # print(aaa)
                        temp.append(aaa)
        # print(temp)
        result = set(list(map(tuple, temp)))
        # print(result)
        print(list(result))
        # return result
