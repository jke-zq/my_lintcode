/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    RandomListNode *copyRandomList(RandomListNode *head) {
        // write your code here
        // RandomListNode *dummy = new RandomListNode(INT_MIN);
        // dummy->next = head;
        // while (head){
        //     auto copy_head = new RandomListNode(head->label);
        //     copy_head->next = head->next;
        //     head->next = copy_head;
        //     head = copy_head->next;
        // }
        // //copy the random poiter
        // head = dummy->next;
        // while(head){
        //     auto copy_head = head->next;
        //     if (head->random){
        //         copy_head->random = head->random->next;
        //     }
        //     head = copy_head->next;
        // }
        
        // //separate
        // head = dummy;
        // RandomListNode *copy_dummy = new RandomListNode(INT_MIN);
        // auto copy_head = copy_dummy;
        // auto p = dummy->next;
        // while (p){
        //     head->next = p;
        //     copy_head->next = p->next;
        //     p = p->next->next;
        //     head = head->next;
        //     copy_head = copy_head->next;
        // }
        // head->next = nullptr;
        // head = dummy->next;
        // return copy_dummy->next;
        //good codes using for-loop
        
        for (RandomListNode *cur = head; cur; cur = cur->next->next){
            auto copy = new RandomListNode(cur->label);
            copy->next = cur->next;
            cur->next = copy;
        }
        //copy random
        for (RandomListNode *cur = head; cur; cur = cur->next->next){
            if (cur->random){
                cur->next->random = cur->random->next;
            }
        }
        //seprate
        RandomListNode dummy(INT_MIN);
        for (RandomListNode *cur = head, *copy = &dummy; cur; cur = cur->next, copy = copy->next){
            copy->next = cur->next;
            cur->next = copy->next->next;
        }
        return dummy.next;
    }
};
