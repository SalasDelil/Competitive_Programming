class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pairs = {}
        least_sum = len(list1) + len(list2)
        cmn_strs = []

        for string in list1:
            if string in list2:
                pairs[list1.index(string)] = list2.index(string)
                least_sum = min(least_sum ,list1.index(string) + list2.index(string))
        
        for key, value in pairs.items():
            if key + value <= least_sum:
                cmn_strs.append(list1[key])
        
        return cmn_strs


