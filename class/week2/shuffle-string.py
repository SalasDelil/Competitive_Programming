class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        chars_arr = ['']*len(indices)

        for i in range(len(indices)):
            chars_arr[indices[i]] = s[i]

        shuffled_str = "".join(chars_arr)
        return shuffled_str