# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def merge(l1, l2):
            newList = ListNode()
            tail = newList

            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next

            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return newList.next

        def mergeSort(lists):
            if not lists:
                return None
            elif len(lists) < 2:
                return lists[0]
            
            # until the size of lists is greater than 1.
            while len(lists) > 1:
                mergedLists = []
                for i in range(0, len(lists), 2):
                    l1 = lists[i]
                    # if 'i' goes out of bound assign null.
                    l2 = lists[i+1] if i+1 < len(lists) else None
                    ''' merging 2 lists and appending into new list
                        after this len(lists)/2 into mergedLists because,
                        after every iteration 2 lists are merging into 1.'''
                    mergedLists.append(merge(l1, l2))
                # assiging new mergedList to lists
                lists = mergedLists
            
            # After merging all list we will get 1 final list with all 
            # values at index 0;
            return lists[0]
        return mergeSort(lists)

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
    ListNode* merge(ListNode* l1, ListNode* l2){
        ListNode* newList = new ListNode();
        ListNode* tail = newList;

        while(l1 != NULL && l2 != NULL){
            if(l1->val <= l2->val){
                tail->next = l1;
                l1 = l1->next;
            }else{
                tail->next = l2;
                l2 = l2->next;
            }
            tail = tail->next;
        }

        if(l1 != NULL)
            tail->next = l1;
        else
            tail->next = l2;

        return newList->next;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) return NULL;
        else if(lists.size() < 2) return lists[0];

        while(lists.size() > 1){
            vector<ListNode*> mergedLists;

            for(int i=0;i<lists.size();i=i+2){
                ListNode* l1 = lists[i];
                ListNode* l2 = NULL;
                if(i+1 < lists.size()) l2 = lists[i+1];

                mergedLists.push_back(merge(l1, l2));
            }
            lists.clear();
            for(auto i:mergedLists)
                lists.push_back(i);
        }

        return lists[0];
    }
};
'''
