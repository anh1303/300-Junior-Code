
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] magMap = new int[26];
        for (char c : magazine.toCharArray())
        {
            magMap[c - 'a']++;
        }
        for (char c : ransomNote.toCharArray())
        {
            if (magMap[c - 'a'] == 0)
            {
                return false;
            }
            else
            {
                magMap[c - 'a']--;
            }
        }
        return true;
    }
}
