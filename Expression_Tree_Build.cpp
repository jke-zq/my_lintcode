
/**
*NOTE:
*     I cant find the solution.After reading other's codes, I write the codes.
*     Actually, I cant understand why or how to find the solution, but how to write the codes.
*     The key point of the solution is the function infixToPrefix. 
*     I dont want to explain the cods, it's self-explain.
*c++ skills:
*     string("aaa").find, before using find func, you must construct the string obj, see more from c++_details/string.
*     string == "" not '', even if it's a char.
*     better using emplace_back/emplace than push_back/push.
*     reverse a vector: reverse(v.begin(), v.end());
*/
/**
 * Definition of ExpressionTreeNode:
 * class ExpressionTreeNode {
 * public:
 *     string symbol;
 *     ExpressionTreeNode *left, *right;
 *     ExpressionTreeNode(string symbol) {
 *         this->symbol = symbol;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param expression: A string array
     * @return: The root of expression tree
     */
    ExpressionTreeNode* build(vector<string> &expression) {
        // write your code here
        if (expression.empty()) return nullptr;
        vector<string> prefix;
        infixToPrefix(expression, prefix);
        int start = 0;
        return buildBinary(prefix, start);
    }
    ExpressionTreeNode* buildBinary(vector<string>& prefix, int& start){
        if(start == prefix.size()) return nullptr;
        // if(prefix.empty()) return nullptr; //this is from the ref codes, but I think this is a bug.
        ExpressionTreeNode* node = new ExpressionTreeNode(prefix[start++]);
        if(isOperator(prefix[start-1])){
            node->left = buildBinary(prefix, start);
            node->right = buildBinary(prefix, start);
        }
        return node;
    }
    void infixToPrefix(vector<string>& infix, vector<string>& prefix){
        reverse(infix.begin(), infix.end());
        stack<string> s;
        for(auto& tok : infix){
            if(tok.size() > 1 || string("+-*/()").find(tok) == string::npos){
                prefix.emplace_back(tok);
            }else if(tok == ")"){
                s.emplace(tok);
            }else if(tok == "("){
                while(!s.empty() && (tok = s.top()) != ")"){
                    s.pop();
                    prefix.emplace_back(tok);
                }
                if(!s.empty()) s.pop();
            }else{
                while(!s.empty() && preference(s.top()) > preference(tok)){
                    prefix.emplace_back(s.top());
                    s.pop();
                }
                s.emplace(tok);
            }
        }
        while(!s.empty()){
            prefix.emplace_back(s.top());
            s.pop();
        }
        reverse(prefix.begin(), prefix.end());
    }
    bool isOperator(string &op){
        return op.size() == 1 && string("+-*/").find(op) != string::npos;
    }
    int preference(string& op){
        if(op == ")"){
            return 0;
        }else if(op == "-" || op == "+"){
            return 1;
        }else if(op == "*" || op == "/"){
            return 2;
        }else{
            return 3;
        }
    }
};

