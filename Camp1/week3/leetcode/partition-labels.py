class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        span = defaultdict(list)
        size = []

        # find the span of each characters
        for i in range(len(s)):
            if s[i] in span:
                span[s[i]][1] = i
            else:
                span[s[i]] = [i,0]
        print(span)

        # count overlapping spans
        l, r = span[s[0]][0], span[s[0]][1]
        for interval in span.values():
            if r >= interval[0] and interval[1] > r:
                r = interval[1]
            elif r < interval[0]:
                if r == 0:
                    size.append(1)
                else:
                    size.append(r-l+1)
                r = interval[1]
                l = interval[0]

        if r == 0:
            size.append(1)
        else:
            size.append(r-l+1)

        return size
