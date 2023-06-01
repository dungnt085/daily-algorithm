from typing import List

def trap(height: List[int]) -> int:
    # height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # max_left =  # 0 0 1 1 2 2 2 2 3 3 3 3 the max heigh on the left handside
    # max_right = # 3 3 3 3 3 3 3 2 2 2 0 0 the max heigh on the right handside

    ans = 0
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    while(left < right):
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                ans += left_max - height[left] 
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                ans += right_max - height[right] 
            right -= 1
    return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))