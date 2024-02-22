class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def build(rowindex):
            if rowindex == 0:
                return [1]

            temp = build(rowindex-1)
            curr_row = [1]

            for i in range(1,len(temp)):
                curr_row.append(temp[i]+temp[i-1])
            curr_row.append(1)
        
            return curr_row
        
        return build(rowIndex)