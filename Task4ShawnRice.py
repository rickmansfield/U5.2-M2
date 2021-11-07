def csFindTheSingleNumber(nums):
    freq = {}
    for n in nums:
        if not n in freq:
            freq[n] = 1
        else:
            freq[n] += 1
    for v in freq:
        if freq[v] ==1:
            return v