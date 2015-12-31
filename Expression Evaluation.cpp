class Solution {
public:
    /**
     * @param expression: a vector of strings;
     * @return: an integer
     */
    int evaluateExpression(vector<string> &expression) {
        // write your code here
        
        if (expression.size() == 1)
        {
            return atoi(expression[0].c_str());
        }
        stack<string> oprs;
        stack<int> opns;
        string operators{"+-*/"};
        int ret = 0;
        for (const auto &e : expression)
        {
            if (operators.find(e) != string::npos)
            {
                while (!oprs.empty() && oprs.top() != "(" && precedence(e) <= precedence(oprs.top()))
                {
                    operateDo(opns, oprs.top(), ret);
                    oprs.pop();
                }
                oprs.emplace(e);
            }
            else if (e == "(")
            {
                oprs.emplace(e);
            }
            else if (e == ")")
            {
                while (!oprs.empty() && oprs.top() != "(")
                {
                    operateDo(opns, oprs.top(), ret);
                    oprs.pop();
                }
                oprs.pop();
            }
            else
            {
                opns.emplace(atoi(e.c_str()));
            }
        }
        while (!oprs.empty())
        {
            operateDo(opns, oprs.top(), ret);
            oprs.pop();
        }
        return ret;
    }
    
    void operateDo(stack<int> &opns, string opr, int &ret)
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
        else
        {
            ret = -1000;
        }
        ret = tmp;
        opns.emplace(tmp);
    }
    
    int precedence(string s)
    {
        if (s == "+" || s == "-")
        {
            return 1;
        }
        else if (s == "*" || s == "/")
        {
            return 2;
        }
        else
        {
            return 3;
        }
    }
};