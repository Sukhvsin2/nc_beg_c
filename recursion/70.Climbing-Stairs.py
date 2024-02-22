class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
        

'''
class Solution {
public:
    int climbStairs(int n) {
        int one = 1, two = 1;

        for(int i=0;i<n-1;i++){
            int temp = one;
            one = one + two;
            two = temp;
        }

        return one;
    }
};
'''
