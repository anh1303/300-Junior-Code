import java.util.HashMap;

class Solution {
    public int longestPalindrome(String s) {
        int len = 0;
        HashMap<Character, Integer> WordCount = new HashMap();
        for (char c: s.toCharArray())
        {
            int count = WordCount.getOrDefault(c, 0) +1 ;
            if (count >= 2)
            {
                count -= 2;
                len += 2;
            }
            WordCount.put(c, count);
        }
        if (len < s.length())
        {
            return len+1;
        }
        return len;
    }
}