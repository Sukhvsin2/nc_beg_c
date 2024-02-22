class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n

        return self.fib(n-1) + self.fib(n-2)

'''
class Solution {
public:
    int fib(int n) {
        if(n <= 1)
            return n;
        
        return fib(n-1) + fib(n-2);
    }
};
'''
