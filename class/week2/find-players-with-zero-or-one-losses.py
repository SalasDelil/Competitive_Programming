class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        matches_result = {}

        for match in matches:
            if match[0] in matches_result:
                matches_result[match[0]][0] += 1
            else:
                matches_result[match[0]] = [1,0]

            if match[1] in matches_result:
                matches_result[match[1]][1] += 1
            else:
                matches_result[match[1]] = [0,1]

        for key, value in matches_result.items():
            if value[0] > 0 and value[1] == 0:
                ans[0].append(key)
            elif value[1] ==1:
                ans[1].append(key)
                
        ans[0] = sorted(ans[0])
        ans[1] = sorted(ans[1])
        return ans

            
