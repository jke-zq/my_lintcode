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
     * @param s: the starting Directed graph node
     * @param t: the terminal Directed graph node
     * @return: a boolean value
     */
    bool hasRoute(vector<DirectedGraphNode*> graph,
                  DirectedGraphNode* s, DirectedGraphNode* t) {
        // write your code here
        return doFind(s, t);
    }
    bool doFind(DirectedGraphNode* s, DirectedGraphNode* t){
        if(s == t) return true;
        for(auto* node : s->neighbors){
            if(doFind(node, t)) return true;
        }
        return false;
        
    }
};


