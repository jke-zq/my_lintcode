
class Solution {
public:
    /**
     * @param a a number
     * @param b a number
     * @return the result
     */
    string addBinary(string& a, string& b) {
        // Write your code here
        int inta = 0;
        int intb = 0;
        int cherry = 0;
        string result = "";
        while(a.size() > 0 && b.size() > 0){
            inta = a.back() == '1' ? 1 : 0;
            intb = b.back() == '1' ? 1 : 0;
            a = a.substr(0, a.size() - 1);
            b = b.substr(0, b.size() - 1);
            cherry = cherry + inta + intb;
            if(cherry >= 0){
                result.insert(0, cherry % 2 == 1 ? "1" : "0");
                cherry = cherry / 2;
            }
        }
        while(a.size() > 0){
            inta = a.back() == '1' ? 1 : 0;
            a = a.substr(0, a.size() - 1);
            cherry = cherry + inta;
            if(cherry >= 0){
                result.insert(0, cherry % 2 == 1 ? "1" : "0");
                cherry = cherry / 2;
            }
        }
        
        while(b.size() > 0){
            intb = b.back() == '1' ? 1 : 0;
            b = b.substr(0, b.size() - 1);
            cherry = cherry + intb;
            if(cherry >= 0){
                result.insert(0, cherry % 2 == 1 ? "1" : "0");
                cherry = cherry / 2;
            }
        }
        
        if(cherry > 0)
            result.insert(0, cherry % 2 == 1 ? "1" : "0");
        return result;
        
    }
};
