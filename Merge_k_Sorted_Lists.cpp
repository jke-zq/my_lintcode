/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        // write your code here
        ListNode dummy(INT_MIN);
        ListNode *cur = &dummy;
        
        priority_queue<ListNode *, vector<ListNode *>, Mycompare> que;
        for (const auto &node : lists)
        {
            if (node != nullptr)
            {
                que.emplace(node);
            }
        }
        
        while (!que.empty())
        {
            auto node = que.top();
            que.pop();
            cur->next = node;
            cur = cur->next;
            if (node->next != nullptr)
            {
                que.emplace(node->next);
            }
        }
        return dummy.next;
        
        
    }
    struct Mycompare{
        bool operator()(const ListNode *l, const ListNode *r)
        {
            return l->val > r->val;
        }
    };
};



