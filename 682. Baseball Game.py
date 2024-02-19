class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = []

        for i in operations:
            if i == 'C':
                if len(res) != 0:
                    res.pop()
            elif i == '+':
                temp = 0
                if len(res) > 1:
                    temp += res[-1]
                    temp += res[-2]
                res.append(temp)
            elif i == 'D':
                if len(res) != 0:
                    temp = 2 * res[-1]
                    res.append(temp)
            else:
                res.append(int(i))
        
        return sum(res)
