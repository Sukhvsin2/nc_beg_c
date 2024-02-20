class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openToClose = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in openToClose:
                if stack and stack[-1] == openToClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        pattern = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        res = []
        for i in s:
            if not res and pattern.get(i):
                return False
            elif pattern.get(i):
                last_item = res.pop()
                if last_item != pattern[i]:
                    return False
                else:
                    continue
            else:
                res.append(i)

        if not res:
            return True
        return False'''
