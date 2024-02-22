class MyStack(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# C++ code here
'''
class MyStack {
    queue<int> q;

public:
    MyStack() {
    }
    
    void push(int x) {
        q.push(x);
    }
    
    int pop() {
        for(int i=0;i<q.size()-1;i++){
            int temp = q.front();
            q.pop();
            q.push(temp);
        }
        int f = q.front();
        q.pop();
        return f;
    }
    
    int top() {
        return q.back();
    }
    
    bool empty() {
        return q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
'''
