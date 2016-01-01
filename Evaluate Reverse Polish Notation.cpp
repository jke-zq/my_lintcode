class Solution {
public:
    /**
     * @param tokens The Reverse Polish Notation
     * @return the value
     */
    int evalRPN(vector<string>& tokens) {
        // Write your code here
        stack<int> s;
        string oprs{"+-*/"};
        for (const auto &tok : tokens)
        {
            if (oprs.find(tok) != string::npos)
            {
                operateDo(s, tok);
            }
            else
            {
                s.emplace(atoi(tok.c_str()));
            }
        }
        
        return s.top();
    }
    void operateDo(stack<int> &opns, string opr)
    {
        int v2 = opns.top();
        opns.pop();
        int v1 = opns.top();
        opns.pop();
        int tmp = 0;
        if (opr == "+")
        {
            tmp = v1 + v2;
        }
        else if (opr == "-")
        {
            tmp = v1 - v2;
        }
        else if (opr == "*")
        {
            tmp = v1 * v2;
        }
        else if (opr == "/")
        {
            tmp = v1 / v2;
        }
        opns.emplace(tmp);
    }
};