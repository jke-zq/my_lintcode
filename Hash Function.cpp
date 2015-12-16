class Solution {
public:
    /**
     * @param key: A String you should hash
     * @param HASH_SIZE: An integer
     * @return an integer
     */
    int hashCode(string key,int HASH_SIZE) {
        // write your code here
        //overflow
        //LONG LONG TYPE MUST BE WITH INIT VALUE
        long long mult = 1L;
        long long ret = 0L;
        for (int i = key.length() - 1; i >= 0; --i)
        {
            ret += static_cast<const long long>(key[i]) * mult;
            mult *= 33;
            mult %= HASH_SIZE;
            ret %= HASH_SIZE;
        }
        return ret % HASH_SIZE;
        
        // long long ret = 0L;
        // for (const auto& k : key)
        // {
        //     ret = ret * 33L % HASH_SIZE;
        //     ret = (ret + static_cast<const long long>(k)) % HASH_SIZE;
        // }
        // return ret;
    }
};