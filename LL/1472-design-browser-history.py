class Node:
    def __init__(self, name):
        self.url = name
        self.prev = None
        self.next = None

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.curr = Node(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr.next = Node(url)
        self.curr.next.prev = self.curr
        self.curr = self.curr.next

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while(steps > 0 and self.curr.prev != None):
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while(steps > 0 and self.curr.next != None):
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
'''
struct Node{
    string url;
    Node* prev, *next;
};

class BrowserHistory {
    Node* head, *curr;
    Node* createNode(string name){
        Node* temp = new Node();
        temp->url = name;
        temp->prev = temp->next = NULL;
        return temp;
    }

    void cleanup(Node* curr){
        Node* temp = NULL;
        while(curr != NULL){
            temp = curr;
            curr = curr->next;
            delete temp;
        }
    }
public:
    BrowserHistory(string homepage) {
        head = createNode(homepage);
        curr = head;
    }
    
    void visit(string url) {
        cleanup(curr->next);
        curr->next = createNode(url);
        curr->next->prev = curr;
        curr = curr->next;
    }
    
    string back(int steps) {
        while(steps > 0 && curr->prev != NULL){
            curr = curr->prev;
            steps--;
        }

        return curr->url;
    }
    
    string forward(int steps) {
        while(steps > 0 && curr->next != NULL){
            curr = curr->next;
            steps--;
        }
        return curr->url;
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */
'''
