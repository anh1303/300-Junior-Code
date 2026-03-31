class Solution {
    public boolean backspaceCompare(String s, String t) 
    {
        if (s == null || t == null) {
            return false;
        }
        String s1 = buildString(s);
        String s2 = buildString(t);
        return s1.equals(s2);
    }

    private String buildString(String str)
    {
        StringBuilder sb = new StringBuilder();
        for (char c : str.toCharArray())
        {
            if (c == '#')
            {
                if (sb.length() > 0)
                {
                    sb.deleteCharAt(sb.length() - 1);
                }
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}