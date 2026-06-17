#container with most water

#brainstorm : converging two pointers tech. 
# start with index beginning and end points. Find area = min(height[left], height[right]) * width (right - left)
#move pointer to shorter height

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #start points to prep for converging points, at both ends. 
        left = 0
        right = len(height) - 1
        maxArea = 0 #final area returned, intialize to 0

        while left <= right: #cycle through array. 
            width = right - left 
            current_area = min(height[left], height[right]) * width
            maxArea = max(maxArea, current_area) #compare current area and maxarea, and if its larger, update it. 
            #move pointer to shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea

