class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        goods = []
        not_goods = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
        
        for i in range(len(fronts)):
            if fronts[i] not in not_goods:
                goods.append(fronts[i])

            if backs[i] not in not_goods:
                goods.append(backs[i])

        goods_list = list(set(goods))
        good_int = 0
        if goods_list != []:
            good_int = goods_list[0]
        else:
            return 0

        for integer in goods_list:
            good_int = min(integer, good_int)

        return good_int