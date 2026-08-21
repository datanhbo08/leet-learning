class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        coins.sort()
        new_coins = []
        for x in coins:
            if all(x % y != 0 for y in new_coins):
                new_coins.append(x)
        
        left = k
        right = new_coins[0] * k 
        

        add_lcm = []
        sub_lcm = []
        
        def dfs(idx: int, current_lcm: int, subset_size: int):
            if subset_size > 0:
                if subset_size % 2 == 1:
                    add_lcm.append(current_lcm)
                else:
                    sub_lcm.append(current_lcm)
            
            for i in range(idx, len(new_coins)):
                c = new_coins[i]
                next_lcm = (current_lcm * c) // math.gcd(current_lcm, c)
                
                if next_lcm <= right:
                    dfs(i + 1, next_lcm, subset_size + 1)

        dfs(0, 1, 0)

        while left < right:
            mid = (left + right) // 2
            
            res = 0
            for l in add_lcm:
                res += mid // l
            for l in sub_lcm:
                res -= mid // l
                
            if res >= k:
                right = mid
            else:
                left = mid + 1
                
        return left