class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        INF = float("inf")
        min_count = INF
        white_count = 0
        left = 0

        for right in range(len(blocks)):
            if right >= k:
                min_count = min(min_count, white_count)
                if blocks[right] == "W":
                    white_count += 1
                if blocks[left] == "W":
                    white_count -= 1
                left += 1
            else:
                if blocks[right] == "W":
                    white_count += 1
                    
        min_count = min(min_count, white_count)

        return min_count if min_count != INF else 0