class Solution {
public:
    /**
     * @param expression: A string array
     * @return: The Reverse Polish notation of this expression
     */
    vector<string> convertToRPN(vector<string> &expression) {
        // write your code here
        vector<string> rpn;
        stack<string> ops;
        string operators{"+-*/"};
        for (const auto &op : expression)
        {
            if (operators.find(op) != string::npos)
            {
                while (!ops.empty() && precedence(op) <= precedence(ops.top()))
                {
                    rpn.emplace_back(ops.top());
                    ops.pop();
                }
                ops.emplace(op);
            }
            else if (op == "(")
            {
                ops.emplace(op);
            }
            else if (op == ")")
            {
                while (!ops.empty() && ops.top() != "(")
                {
                    rpn.emplace_back(ops.top());
                    ops.pop();
                }
                ops.pop();
            }
            else
            {
                rpn.emplace_back(op);
            }
        }
        while (!ops.empty())
        {
            rpn.emplace_back(ops.top());
            ops.pop();
        }
        return rpn;
    }
    
    int precedence(string op)
    {
        if (op == "+" || op == "-")
        {
            return 1;
        }
        else if (op == "*" || op == "/")
        {
            return 2;
        }
        else
        {
            return 0;
        }
    }
};