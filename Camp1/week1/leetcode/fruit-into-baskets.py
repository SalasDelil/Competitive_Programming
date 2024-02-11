class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = defaultdict(int)
        ans, left = 0, 0

        for right, typ in enumerate(fruits):
            cnt[typ] += 1

            while len(cnt) > 2:
                cnt[x := fruits[left]] -= 1

                if cnt[x] == 0:
                    cnt.pop(x)

                left += 1

            ans = max(ans, right - left + 1)

        return ans