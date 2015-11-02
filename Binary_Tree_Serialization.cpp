/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */
class Solution {
private:
    bool getNumber(const string &data, int &start, int &num)
    {
        if (data[start] == '#')
        {
            start += 2;
            return false;
        }
        num = 0;
        while (data[start] != ' ')
        {
            num = num * 10 + data[start++] - '0';
        }
        ++start;
        return true;
    }
    
    void deserializeHelper(TreeNode *&root, int &start, const string &data)
    {
        int num;
        if (!getNumber(data, start, num))
        {
            root = nullptr;
            return;
        }
        root = new TreeNode(num);
        deserializeHelper(root->left, start, data);
        deserializeHelper(root->right, start, data);
    }
    
    void serializeHelper(TreeNode *root, string &output)
    {
        if (!root)
        {
            output += "# ";
            return;
        }
        else 
        {
            stringstream buffer;
            buffer << root->val << " ";
            output += buffer.str();
            serializeHelper(root->left, output);
            serializeHelper(root->right, output);
        }
    }
public:
    /**
     * This method will be invoked first, you should design your own algorithm 
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    string serialize(TreeNode *root) {
        // write your code here
        string output;
        serializeHelper(root, output);
        return output;
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in 
     * "serialize" method.
     */
    TreeNode *deserialize(string data) {
        // write your code here
        int start = 0;
        TreeNode *root;
        deserializeHelper(root, start, data);
        return root;
    }
};

