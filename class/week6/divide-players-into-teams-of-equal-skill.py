class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot_skill = skill[0] + skill[-1]
        chem_sum = skill[0]*skill[-1]
        left, right = 1, len(skill)-2

        while left < right:
            if skill[left] + skill[right] == tot_skill:
                chem_sum += skill[left]*skill[right]
                left += 1
                right -=1
            else:
                return -1

        return chem_sum