import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int maxLength = 1;
        int start = 0;
        int end = 0;
        if (s.length() == 0){
            return 0;
        }
        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if (map.containsKey(c) && map.get(c) >= start)
            {
                start = map.get(c) + 1;
            }
            map.put(c, i);
            end = i;
            maxLength = Math.max(maxLength, end - start + 1);
        }
        return maxLength;
    }
}