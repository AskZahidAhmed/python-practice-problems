from typing import List

class Solution:
	def longest_consecutive_sequence(self, nums:List[int]) -> int:
		if not nums:
			return 0

		numSet = set(nums)
		longestLength = 0

		for i in numSet: # numSet = [5, 100, 4, 200, 1, 3, 2]
			if (i - 1) not in numSet:  # Check if the current number is the start of a sequence
				currentNum = i
				currentLength = 0

				while (currentLength + 1) in numSet:
					currentNum += 1
					currentLength += 1
		longestLength = max(longestLength, currentLength)

		return longestLength
solution = Solution()
# Example usage
nums = [5, 100, 4, 200, 1, 3, 2]
print(solution.longest_consecutive_sequence(nums))  # Output should be 4

