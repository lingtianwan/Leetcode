# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new = self.heapSort(nums, len(nums))
        return new[k-1]

    def heapSort(self, nums, n):
        self.constructHeap(nums, n)
        i = n - 1
        sorted_arr = []
        while i >= 0:
            sorted_arr.append(nums[0])
            nums[0], nums[i] = nums[i], nums[0]
            self.downshift(nums, i, 0)
            i -= 1
        return sorted_arr

    def constructHeap(self, nums, n):
        parent = (n - 2) / 2
        for i in range(parent, -1, -1):
            self.downshift(nums, n ,i)

    def downshift(self, nums, n, parent):
        if parent < 0:
            return
        left = parent * 2 + 1
        right = parent * 2 + 2
        if left >= n:
            return
        if right >= n:
            mxch = left
        else:
            if nums[left] >= nums[right]:
                mxch = left
            else:
                mxch = right
        if nums[parent] < nums[mxch]:
            nums[parent], nums[mxch] = nums[mxch], nums[parent]
            self.downshift(nums, n, mxch)
