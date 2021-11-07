
"""
initiate an empty array/list set to variable "S" for single
Loop over provided nums list 
If eachNum in num not in nums:
    add to new empty list
return conveted list to string
"""
# this solution is too difficult with out hash tables. So I skipped finishing it. 
# import builtins
# # print(dir(builtins))
# # print(help(str))
# def csFindTheSingleNumber3(nums):
#     s = []
#     for eachNum in nums:
#         # print(eachNum)
#         if eachNum not in s:
#             s.append(eachNum)
#         else:
#             s.remove(eachNum)
#         # print(s)
#     return s.pop()

# This is the ideal solition for class
# print(help(dict.items))

# def csFindTheSingleNumber(nums):
#     frequency = {}
#     for num in nums:
#         if num not in frequency:
#             frequency[num] = 1
#             # print(frequency)
#         else:
#             frequency[num] +=1
#     for (num, freq) in frequency.items():
#         # print(frequency.items())
#         if freq == 1:
#             return num
#     return -1

# alternative after researching built in fuctions better for real world
from collections import Counter
def csFindTheSingleNumber2(nums):
    frequency = Counter(nums)
    print(frequency)
    for i in frequency:
        if frequency[i] == 1:
            return i

# print(csFindTheSingleNumber([1,1,2,1]))
print(csFindTheSingleNumber2([1,1,2,1]))
# print(csFindTheSingleNumber3([1,1,2,1]))