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
     * @param hashTable: A list of The first node of linked list
     * @return: A list of The first node of linked list which have twice size
     */    
    vector<ListNode*> rehashing(vector<ListNode*> hashTable) {
        // write your code here
        int old_size = hashTable.size();
        vector<ListNode *> rehashTable(old_size * 2, nullptr);
        for (int i = 0; i < old_size; ++i)
        {
            dorehash(hashTable[i], rehashTable);
        }
        return rehashTable;
    }
    
    void dorehash(ListNode *node, vector<ListNode *> &rehashTable)
    {
        ListNode *cur = node;
        int size = rehashTable.size();
        while (cur)
        {
            int index = (cur->val % size + size) % size;
            if (!rehashTable[index])
            {
                rehashTable[index] = new ListNode(cur->val);
            }
            else
            {
                ListNode *tmp = rehashTable[index];
                while (tmp->next)
                {
                    tmp = tmp->next;
                }
                tmp->next = new ListNode(cur->val);
            }
            cur = cur->next;
        }
    }
};
