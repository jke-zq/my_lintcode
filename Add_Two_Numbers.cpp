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
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2 
     */
    ListNode *addLists(ListNode *l1, ListNode *l2) {
        // write your code here
        //big integer overflow.
        // long long left = 0;
        // int tens = 0;
        // while(l1){
        //     left += pow(10, tens) * l1->val;
        //     ++tens;
        //     l1 = l1->next;
        // }
        // long long right = 0;
        // tens = 0;
        // while(l2){
        //     right += pow(10, tens) * l2->val;
        //     ++tens;
        //     l2 = l2->next;
        // }
        // long long sum = left + right;//overflow ??
        // ListNode* result = new ListNode(-1);
        // ListNode* dummy = result;
        // // if(sum == 0) return new ListNode(0);
        // while(sum >= 0){
        //     result->next = new ListNode(sum % 10);
        //     result = result->next;
        //     sum = sum / 10;
        //     if(sum == 0) break;
        // }
        // return dummy->next;
        ListNode* dummy = new ListNode(-1);
        ListNode* result = dummy;
        int left = 0;
        int right = 0;
        int cherry = 0;
        while(l1 || l2 || cherry){
            left = l1 ? l1->val : 0;
            right = l2 ? l2->val : 0;
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
            cherry += left + right;
            if(cherry >= 0){
                result->next = new ListNode(cherry % 10);
                result = result->next;
                cherry /= 10;
            }else break;
        }
        return dummy->next;
    }
};
