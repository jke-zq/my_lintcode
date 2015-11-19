class Queue {
public:
    stack<int> stack1;
    stack<int> stack2;

    Queue() {
        // do intialization if necessary
    }

    void push(int element) {
        // write your code here
        stack1.emplace(element);
    }
    
    int pop() {
        // write your code here
        int ret = top();
        stack2.pop();
        return ret;
    }

    int top() {
        // write your code here
        if (stack2.empty())
        {
            while (!stack1.empty())
            {
                stack2.emplace(stack1.top());
                stack1.pop();
            }
        }
        return stack2.top();
    }
};

