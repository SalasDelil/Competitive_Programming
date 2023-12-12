class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        ans = []
        
        #first let's take the sum of all even numbers
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        #then iterate over all the queries
        for query in queries:
            val, index = query
            if (nums[index] + val) % 2 == 0:
                if nums[index] % 2 == 0:
                    even_sum += val
                    ans.append(even_sum)
                else:
                    even_sum += (nums[index] + val)
                    ans.append(even_sum)
                
                nums[index] = nums[index] + val
            else:
                if nums[index] % 2 == 0:
                    even_sum -= nums[index]
                    ans.append(even_sum)
                else:
                    ans.append(even_sum)

                nums[index] = nums[index] + val

        return ans
