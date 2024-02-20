# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def createNode(val):
        temp = ListNode(val)
        return temp

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode()
        tail = newList

        tL1 = list1
        tL2 = list2

        while tL1 and tL2:
            if tL1.val <= tL2.val:
                tail.next = ListNode(tL1.val)
                tL1 = tL1.next
            else:
                tail.next = ListNode(tL2.val)
                tL2 = tL2.next

            tail = tail.next
        
        while tL1:
            tail.next = ListNode(tL1.val)
            tL1 = tL1.next
            tail = tail.next

        while tL2:
            tail.next = ListNode(tL2.val)
            tL2 = tL2.next
            tail = tail.next
        
        return newList.next

'''
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

    ListNode* createNode(int data){
        ListNode *temp = new ListNode(data);
        return temp;
    }

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* tempL1 = list1, *tempL2 = list2;

        ListNode *newList = new ListNode(), *tail = newList;

        while(tempL1 != NULL && tempL2 != NULL){
            if(tempL1->val <= tempL2->val){
                tail->next = new ListNode(tempL1->val);
                tempL1 = tempL1->next;
            }else{
                tail->next = new ListNode(tempL2->val);
                tempL2 = tempL2->next;
            }

            tail = tail->next;
        }

        while(tempL1 != NULL){
            tail->next = new ListNode(tempL1->val);
            tempL1 = tempL1->next;
            tail = tail->next;
        }
        while(tempL2 != NULL){
            tail->next = new ListNode(tempL2->val);
            tempL2 = tempL2->next;
            tail = tail->next;
        }
        return newList->next;
    }
};
'''
