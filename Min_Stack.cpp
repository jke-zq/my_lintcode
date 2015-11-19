class MinStack {
private:
    stack<int> min_stack;
    stack<int> data;
public:
    MinStack() {
        // do initialization if necessary
    }

    void push(int number) {
        // write your code here
        if (min_stack.empty() || min_stack.top() >= number)
        {
            min_stack.emplace(number);
        }
        data.emplace(number);
    }

    int pop() {
        // write your code here
        int number = data.top();
        if (number == min_stack.top())
        {
            min_stack.pop();
        }
        data.pop();
        return number;
    }

    int min() {
        // write your code here
        if (!min_stack.empty())
        {
            return min_stack.top();
        }
    }
};

