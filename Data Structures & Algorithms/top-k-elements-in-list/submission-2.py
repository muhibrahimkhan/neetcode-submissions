class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        size_of_each = {}
        for num in nums:
            if num not in size_of_each:
                size_of_each[num] = 0
            size_of_each[num] += 1
    

        arr = []
        for num, count in size_of_each.items():
            arr.append([count, num])
        arr.sort()

        result = []
        while k > len(result):
            num = arr.pop()[1]
            result.append(num)
        
        return result