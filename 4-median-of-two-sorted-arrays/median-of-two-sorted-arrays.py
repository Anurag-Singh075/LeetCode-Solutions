class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge_array(left, right):
            result = []
            i = j = 0
            n, m = len(left), len(right)
            while i < n and j < m:
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while i < n:
                result.append(left[i])
                i += 1
            while j < m:
                result.append(right[j])
                j += 1
            return result
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge_array(left, right)
        merged = nums1 + nums2
        merged = merge_sort(merged)
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
