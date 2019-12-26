class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_dict:
                num_dict[nums[i]].append(i)
            else:
                num_dict[nums[i]] = [i]

        for key in num_dict:
            complement = target - key
            if complement in num_dict and complement != key:
                return [num_dict[key][0], num_dict[complement][0]]

            elif complement in num_dict and complement == key and len(num_dict[complement]) > 1:
                return [num_dict[key][0], num_dict[key][1]]