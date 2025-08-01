class Solution:
  def bruteForce(self, nums, k):
    n = len(nums)
        #brute-force Solution
        # dic = defaultdict(int)
        subArray = 0
        seen = set()
        for left in range(n):
            seen = set()
            for right in range(left, n):
                seen.add(nums[right])
                if len(seen) > k:
                    break
                elif len(seen) == k:
                    subArray += 1
        return subArray
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
      # return self.bruteForce(nums, k)
      return self.solve(nums, k) - self.solve(nums, k-1)

    def solve(self, nums, distinctK):
        dic = defaultdict(int)
        count = left = 0
        n = len(nums)
        for right in range(n):
            dic[nums[right]] += 1
            while len(dic) > distinctK:
                dic[nums[left]] -= 1
                if dic[nums[left]] == 0:
                    del dic[nums[left]]
                left += 1
            count += right - left +1
            
        return count
      
      
        


        
