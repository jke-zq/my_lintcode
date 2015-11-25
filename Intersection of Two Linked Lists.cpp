/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param headA: the first list
     * @param headB: the second list
     * @return: a ListNode
     */
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // write your code here
        ListNode dummyA(INT_MIN);
        ListNode dummyB(INT_MIN);
        dummyA.next = headA;
        dummyB.next = headB;
        headA = &dummyA;
        headB = &dummyB;
        while (headA && headB)
        {
            headA = headA->next;
            headB = headB->next;
        }
        ListNode *newHead = nullptr;
        if (headA)
        {
            newHead = &dummyA;
            while (headA)
            {
                headA = headA->next;
                newHead = newHead->next;
            }
            headA = newHead;
            headB = &dummyB;
        }
        else if(headB)
        {
            newHead = &dummyB;
            while (headB)
            {
                headB = headB->next;
                newHead = newHead->next;
            }
            headB = newHead;
            headA = &dummyA;
        }
        else
        {
            headA = &dummyA;
            headB = &dummyB;
        }
        
        while (headA && headB && headA != headB)
        {
            headA = headA->next;
            headB = headB->next;
        }
        
        if (headA == headB)
        {
            return headA;
        }
        else
        {
            return nullptr;
        }
    }
};
