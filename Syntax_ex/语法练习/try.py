# coding=utf-8
def sum(nums):
    # 通过创建新列表,动态求和
    list = []
    for emt in nums:
        s = 0
        for add in nums[0:nums.index(emt)+1]:
            s += add
        list.append(s)
    return list
    
print(sum([145,56,354,65,]))

