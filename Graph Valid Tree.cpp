class Solution {
public:
    /**
     * @param n an integer
     * @param edges a list of undirected edges
     * @return true if it's a valid tree, or false
     */
    bool validTree(int n, vector<vector<int>>& edges) {
        // Write your code here
        if (edges.size() != n - 1)
        {
            return false;
        }
        vector<vector<int>> graph(n);
        
        for (const auto& e : edges)
        {
            graph[e[0]].emplace_back(e[1]);
            graph[e[1]].emplace_back(e[0]);
        }
        //cant judge whether there is a circle or not.
        queue<int> q;
        q.emplace(0);
        vector<bool> visited(n, false);
        visited[0] = true;
        map<int, int> parent;
        while (!q.empty())
        {
            int root = q.front();
            q.pop();
            for (const auto& neighbor : graph[root])
            {
                if (!visited[neighbor])
                {
                    visited[neighbor] = true;
                    q.emplace(neighbor);
                    parent[neighbor] = root;
                }
                else if (parent.find(root) == parent.end() || neighbor != parent[root])
                {
                    return false;   
                }

            }
        }
        // using dfs to judge whether there is a circle
        // dfs(graph, visited, 0, );
        bool ret = true;
        for (auto v : visited)
        {
            ret &= v;
        }
        return ret;
    }
    void dfs(vector<vector<int>> &graph, vector<bool> &visited, int node)
    {
        if (visited[node])
        {
            return;
        }
        else
        {
            visited[node] = true;
            for (const auto& n : graph[node])
            {
                dfs(graph, visited, n);
            }
        }
    }
};