/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    /**
     * @param node: A undirected graph node
     * @return: A undirected graph node
     */
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        // write your code here
        unordered_map<const UndirectedGraphNode *, UndirectedGraphNode *> map;
        // return doCloneDFS(node, map);
        if (!node)
        {
            return nullptr;
        }
        doCloneBFS(node, map);
        return map[node];
    }
    void doCloneBFS(UndirectedGraphNode *node, unordered_map<const UndirectedGraphNode *, UndirectedGraphNode *> &map)
    {
        queue<const UndirectedGraphNode *> que;
        que.emplace(node);
        map[node] = new UndirectedGraphNode(node->label);
        while (!que.empty())
        {
            auto old_node = que.front();
            que.pop();
            for (const auto &n : old_node->neighbors)
            {
                if (map.find(n) == map.end())
                {
                    map[n] = new UndirectedGraphNode(n->label);
                    que.emplace(n);
                }
                map[old_node]->neighbors.emplace_back(map[n]);
            }
        }
        
    }
    
    UndirectedGraphNode *doCloneDFS(UndirectedGraphNode *node, unordered_map<UndirectedGraphNode *, UndirectedGraphNode *> &map)
    {
        if (!node)
        {
            return nullptr;
        }
        if (map.count(node) == 0)
        {
            auto new_node = new UndirectedGraphNode(node->label);
            map[node] = new_node;
            for (auto &n : node->neighbors)
            {
                new_node->neighbors.emplace_back(doCloneDFS(n, map));
            }
            return new_node;
        }
        else
        {
            return map[node];
        }
    }
};
