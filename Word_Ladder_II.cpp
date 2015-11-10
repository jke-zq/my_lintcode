class Solution {
public:
    /**
      * @param start, a string
      * @param end, a string
      * @param dict, a set of string
      * @return a list of lists of string
      */
    vector<vector<string>> findLadders(string start, string end, unordered_set<string> &dict) {
        // write your code here
        
        // //Time Limit Exceeded
        // unordered_set<string> visited;
        // vector<vector<string>> all_solution;
        // vector<string> solution;
        // solution.emplace_back(start);
        // visited.insert(start);
        // helper(start, end, solution, visited, dict, all_solution);
        // //remove other solution
        // size_t step = INT_MAX;
        // for (auto &s : all_solution)
        // {
        //     step = min(step, s.size());
        // }
        // for (int i = 0; i < all_solution.size();)
        // {
        //     if (all_solution[i].size() != step)
        //     {
        //         all_solution.erase(all_solution.begin() + i);
        //     }
        //     else
        //     {
        //         ++i;
        //     }
        // }
        // return all_solution;
        //find the short path with traceBack, but should remove the unordered_set<string> visited because of the shared head.
        // queue<string> que;
        // que.emplace(start);
        // unordered_set<string> visited;
        // visited.insert(start);
        // unordered_map<string, unordered_set<string>> traceBack;
        // bool toEnd = false;
        // while (!que.empty())
        // {
        //     int qsize = que.size();
        //     while (qsize--)
        //     {
        //         string source = que.front();
        //         que.pop();

        //         for (int i = 0; i < source.length(); ++i)
        //         {
        //             string candidate(source);
        //             for (char j = 'a'; j <= 'z'; ++j)
        //             {
        //                 if (source[i] == j)
        //                 {
        //                     continue;
        //                 }
        //                 candidate[i] = j;
        //                 if (candidate == end || (visited.count(candidate) == 0 && dict.count(candidate) == 1))
        //                 {
        //                     if (candidate == end)
        //                     {
        //                         toEnd = true;
        //                     }
        //                     que.emplace(candidate);
        //                     visited.insert(candidate);
        //                     traceBack[candidate].insert(source);
        //                 }
        //             }
        //         }
        //     }
        //     if (toEnd)
        //     {
        //         break;
        //     }

        // }
        // vector<vector<string>> ret;
        // vector<string> solution;
        // findAllSolution(traceBack, solution, end, ret);
        // return ret;
        //using two vector to BFS the solution.
        unordered_set<string> levels[2];
        int current_level = 0;
        levels[current_level].insert(start);
        unordered_map<string, unordered_set<string>> trace;
        //dict.size() > 0  this condition can be removed becasuse of there must be one solution.
        while (dict.size() > 0 && levels[current_level % 2].size() > 0)
        {
            if (levels[current_level % 2].count(end) > 0)
            {
                break;
            }
            for (string s : levels[current_level % 2])
            {
                dict.erase(s);
            }
            for (string s : levels[current_level % 2])
            {
                for (int i = 0; i < s.length(); ++i)
                {
                    string candidate(s);
                    for (char j = 'a'; j <= 'z'; ++j)
                    {
                        if (s[i] == j)
                        {
                            continue;
                        }
                        candidate[i] = j;
                        if (dict.count(candidate) > 0)
                        {
                            levels[(current_level + 1) % 2].insert(candidate);
                            trace[candidate].insert(s);
                        }
                    }
                }
            }
            levels[current_level % 2].clear();
            ++current_level;
        }
        vector<vector<string>> ret;
        vector<string> tmp;
        findAllSolution(trace, tmp, end, ret);
        return ret;
    }
    
    void findAllSolution(unordered_map<string, unordered_set<string>> &traceBack, vector<string> &solution, string child, vector<vector<string>> &ret)
    {
        solution.emplace_back(child);
        if (traceBack.count(child) == 0)
        {
            vector<string> tmp(solution);
            reverse(tmp.begin(), tmp.end());
            ret.emplace_back(tmp);
        }
        else
        {
            for (string s : traceBack[child])
            {
                findAllSolution(traceBack, solution, s, ret);
            }
        }
        solution.pop_back();
        
    }
    void helper(string start, string &end, vector<string> &solution, unordered_set<string> &visited, unordered_set<string> &dict, vector<vector<string>> &all_solution)
        {
            if (start == end)
            {
                all_solution.emplace_back(solution);
                return;
            }
            if (visited.size() == dict.size())
            {
                return;
            }

            for (int i = 0; i < start.length(); ++i)
            {
                string candidate(start);
                for (char j = 'a'; j <= 'z'; ++j)
                {
                    if (start[i] == j)
                    {
                        continue;
                    }
                    candidate[i] = j;
                    if (visited.count(candidate) == 0 && dict.count(candidate) == 1)
                    {
                        solution.emplace_back(candidate);
                        visited.insert(candidate);
                        helper(candidate, end, solution, visited, dict, all_solution);
                        visited.erase(candidate);
                        solution.pop_back();
                    }
                }
            }
        }
};
