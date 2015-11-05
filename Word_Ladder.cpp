class Solution {
public:
    /**
      * @param start, a string
      * @param end, a string
      * @param dict, a set of string
      * @return an integer
      */
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        // write your code here
        //using queue.size instead of "#" is better.
        // queue<string> queue;
        // queue.emplace(start);
        // queue.emplace("#");
        // int step = 0;
        // while (!queue.empty())
        // {
        //     string s = queue.front();
        //     queue.pop();
        //     if (s == "#")
        //     {
        //         ++step;
        //         if (!queue.empty())
        //         {
        //             queue.emplace("#");
        //         }
        //         continue;
        //     }
        //     if (s == end)
        //     {
        //         return ++step;
        //     }
        //     for (int i = 0; i < s.length(); ++i)
        //     {
        //         string candidate(s);
        //         for (char j = 'a'; j <= 'z'; ++j)
        //         {
        //             if (s[i] == j)
        //             {
        //                 continue;
        //             }
        //             candidate[i] = j;
        //             if (dict.count(candidate) == 1)
        //             {
        //                 dict.erase(candidate);
        //                 queue.emplace(candidate);
        //             }
        //         }
        //     }
        // }
        // return 0;
        //using two vector or queue, when using queue, it's better to use queue.size() as spliter
        queue<string> queue;
        queue.emplace(start);
        unordered_set<string> visited;
        int step = 0;
        while (!queue.empty())
        {
            int qsize = queue.size();
            while (qsize--)
            {
                string word = queue.front();
                queue.pop();
                if (word == end)
                {
                    return ++step;
                }
                for (int i = 0; i < word.length(); ++i)
                {
                    string candidate(word);
                    for (char j = 'a'; j <= 'z'; ++j)
                    {
                        if (word[i] == j)
                        {
                            continue;
                        }
                        candidate[i] = j;
                        if (visited.count(candidate) == 0 && dict.count(candidate) == 1)
                        {
                            queue.emplace(candidate);
                            visited.insert(candidate);
                        }
                    }
                }
            }
            ++step;
        }
        return 0;
    }
};
