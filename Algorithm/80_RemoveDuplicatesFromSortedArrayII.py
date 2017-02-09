# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        dup_count = 1
        total_count = 0
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                dup_count += 1
                if dup_count <= 2:
                    total_count += 1
                    nums[total_count] = nums[i]
            else:
                dup_count = 1
                total_count += 1
                nums[total_count] = nums[i]
        return total_count + 1
