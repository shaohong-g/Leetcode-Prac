


def merge_sort(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    last_pointer = m + n - 1
    num1_pointer = m - 1
    num2_pointer = n - 1

    while num2_pointer >= 0 :
        if num1_pointer < 0 or nums2[num2_pointer] > nums1[num1_pointer]:
            nums1[last_pointer] = nums2[num2_pointer]
            num2_pointer -= 1
        else:
            nums1[last_pointer] = nums1[num1_pointer]
            num1_pointer -= 1
        last_pointer -= 1

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        last_pointer = len(nums) - 1
        first_pointer = 0

        # CORNER CASE if nums = []
        if last_pointer < 0:
            return 0

        while first_pointer <= last_pointer:
            if nums[first_pointer] == val:
                nums[first_pointer] = nums[last_pointer]
                last_pointer -= 1
            else:
                first_pointer += 1

        return first_pointer