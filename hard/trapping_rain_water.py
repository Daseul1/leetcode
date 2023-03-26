class Solution:
    def trap(self, height: List[int]) -> int:
        # height 가 없을때 얘외처리
        if not height:
            return 0

        count = 0 # 물 양
        left, right = 0, len(height) - 1 # 가장 왼쪽, 가장 오른쪽 할당 -> 현재의 높이
        left_max, right_max = height[left], height[right] # 좌우 최대 높이 할당

        while left < right:
            # 좌,우 최대 높이 재할당
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            # 최대 높이 - 현재 높이로 물 양을 구해주고, 투포인터 이동
            if left_max < right_max:
                count += left_max - height[left]
                left += 1
            else: 
                count += right_max - height[right]
                right -= 1
        return count
