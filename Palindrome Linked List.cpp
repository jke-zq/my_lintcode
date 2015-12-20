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
     * @param head a ListNode
     * @return a boolean
     */
    bool isPalindrome(ListNode* head) {
        // Write your code here
        if (!head)
        {
            return true;
        }
        ListNode dummy(INT_MIN);
        dummy.next = head;
        ListNode *fast = &dummy;
        ListNode *slow = &dummy;
        while (fast->next && fast->next->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        slow = slow->next;
        ListNode *last = slow;
        ListNode *right_left = slow->next;
        while (right_left)
        {
            ListNode *tmp_right = right_left;
            right_left = right_left->next;
            tmp_right->next = last;
            last = tmp_right;
        }
        // return true;
        ListNode *first = head;
        while (first != last)
        {
            if (first->val != last->val)
            {
                return false;
            }
            if (first->next == last)
            {
                return true;
            }
            first = first->next;
            last = last->next;
        }
        return true;
    }
};