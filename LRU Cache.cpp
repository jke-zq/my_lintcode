#include <list>
class LRUCache{
private:
    size_t m_capacity;
    unordered_map<int, list<pair<int, int>>::iterator> m_map;
    list<pair<int, int>> m_list;
public:
    // @param capacity, an integer
    LRUCache(int capacity):m_capacity(capacity){
        // write your code here
    }
    
    // @return an integer
    int get(int key) {
        // write your code here
        auto found = m_map.find(key);
        if (found == m_map.end())
        {
            return -1;
        }
        else
        {
            m_list.splice(m_list.begin(), m_list, found->second);
            return found->second->second;
        }
        
    }

    // @param key, an integer
    // @param value, an integer
    // @return nothing
    void set(int key, int value) {
        // write your code here
        auto found = m_map.find(key);
        if (found != m_map.end())
        {
            found->second->second = value;
            m_list.splice(m_list.begin(), m_list, found->second);
        }
        else {
            if (m_map.size() == m_capacity)
            {
                int key_to_del = m_list.back().first;
                m_list.pop_back();
                m_map.erase(key_to_del);
            }
            m_list.emplace_front(key, value);
            m_map[key] = m_list.begin();
        }
    }
};