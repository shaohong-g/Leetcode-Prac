


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

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if (len(nums) < 2):
        return len(nums)

    current_idx = 0

    for i in range(1, len(nums)):
        # swap if moving > curr
        if nums[i] > nums[current_idx]:
            current_idx += 1
            nums[current_idx] = nums[i]

    return current_idx +1

def removeDuplicates2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if (len(nums) <= 2):
        return len(nums)

    current_idx = 1
    for i in range(2, len(nums)):
        if nums[i] != nums[current_idx -1]:
            current_idx += 1
            nums[current_idx] = nums[i]
    return current_idx +1

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Sort solution
    # return sorted(nums)[len(nums)//2]
    
    # Boyer–Moore majority vote algorithm
    candidate = None
    vote = 0

    for each_num in nums:
        if vote == 0:
            candidate = each_num
        vote += (1 if each_num == candidate else -1)
    return candidate

def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k] # O(n) time - O(n) space (concat)

    # Alternative O(n) time -  O(1) space
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    start = prices[0]

    for price in prices[1:]:
        if price < start:
            start = price
        else:
            profit = price - start
            if profit > max_profit:
                max_profit = profit
    return max_profit
def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # O(n^2) O(n)
    if len(nums) == 1:
        return True
    target = len(nums) - 1
    dp_list = [False] * len(nums)
    dp_list[0] = True

    for i in range(len(nums) - 1):
        if not dp_list[i]:
            continue
        for each_jump in range(nums[i]):
            reach = each_jump + i + 1
            if reach < target:
                dp_list[reach] = True
            elif reach == target:
                return True
            elif reach > target:
                break
    return dp_list[-1]

    # Alternative (faster and simpler) O(n) O(1)
    n = len(nums)

    goal = n - 1 

    for i in range(n - 2, -1, -1):
        if nums[i] + i >= goal:
            goal = i
            
    return goal == 0

def jump( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    target = len(nums) - 1
    dp_list = [0] * len(nums)

    for i in range(len(nums) - 1):
        if dp_list[i] == 0 and i != 0:
            continue
        for each_jump in range(nums[i]):
            reach = each_jump + i + 1
            if reach <= target:
                if dp_list[reach] == 0:
                    dp_list[reach] = dp_list[i] + 1
                else:
                    dp_list[reach] = min(dp_list[i] + 1, dp_list[reach])
            elif reach > target:
                break
    return dp_list[-1]