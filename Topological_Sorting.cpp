/**
 * Definition for Directed graph.
 * struct DirectedGraphNode {
 *     int label;
 *     vector<DirectedGraphNode *> neighbors;
 *     DirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    vector<DirectedGraphNode*> topSort(vector<DirectedGraphNode*> graph) {
        // write your code here
        //BFS and DFS
        ////BSF
        // vector<DirectedGraphNode*> output;
        // unordered_map<DirectedGraphNode *, int> ancestor;
        // findAncestorBFS(graph, ancestor);
        // topsortBFS(graph, ancestor, output);
        // return output;
        ////DFS
        vector<DirectedGraphNode *> output;
        unordered_set<DirectedGraphNode *> visited;
        unordered_map<DirectedGraphNode *, unordered_set<DirectedGraphNode *>> ancestor;
        for (auto &node : graph)
        {
            findAncestorDFS(node, visited, ancestor);
        }
        
        visited.clear();
        for (auto &node :graph)
        {
            topsortDFS(node, visited, ancestor, output);
        }
        return output;
    }
    
private:
    void findAncestorDFS(DirectedGraphNode *node, unordered_set<DirectedGraphNode *> &visited, unordered_map<DirectedGraphNode *, unordered_set<DirectedGraphNode *>> &ancestor)
    {
        if (visited.insert(node).second)
        {
            for (auto &neighbor : node->neighbors)
            {
                ancestor[neighbor].insert(node);
                findAncestorDFS(neighbor, visited, ancestor);
            }
        }
    }
    
    void topsortDFS(DirectedGraphNode *node, unordered_set<DirectedGraphNode *> &visited, unordered_map<DirectedGraphNode *, unordered_set<DirectedGraphNode *>> &ancestor, vector<DirectedGraphNode *> &output)
    {
        if (visited.insert(node).second)
        {
            for (auto &ance : ancestor[node])
            {
                topsortDFS(ance, visited, ancestor, output);
            }
            output.emplace_back(node);
        }
    }
    
    void findAncestorBFS(vector<DirectedGraphNode *> &graph, unordered_map<DirectedGraphNode *, int> &ancestor)
    {
       unordered_set<DirectedGraphNode *> visited;
       queue<DirectedGraphNode *> que;
       for (auto &node : graph)
       {
           if (!visited.insert(node).second)
           {
               continue;
           }
           que.emplace(node);
           while (!que.empty())
           {
               auto qnode = que.front();
               que.pop();
               for (auto &n : qnode->neighbors)
               {
                   ++ancestor[n];
                   if (visited.insert(n).second)
                   {
                       que.emplace(n);
                   }
               }
           }
       }
    }
    
    void topsortBFS(vector<DirectedGraphNode *> &graph, unordered_map<DirectedGraphNode *, int> &ancestor, vector<DirectedGraphNode *> &output)
    {
        queue<DirectedGraphNode *> que;
        
        for (auto &node : graph)
        {
            if (ancestor[node] == 0)
            {
                que.emplace(node);
            }
        }
        while (!que.empty())
        {
            auto node = que.front();
            que.pop();
            output.emplace_back(node);
            for (auto &neighbor : node->neighbors)
            {
                --ancestor[neighbor];
                if (ancestor[neighbor] == 0)
                {
                    que.emplace(neighbor);
                }
            }
        }
    }
};
