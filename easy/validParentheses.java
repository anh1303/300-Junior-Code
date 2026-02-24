import java.util.HashMap;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> parenMap = new HashMap<>();
        parenMap.put('(', ')');
        parenMap.put('{', '}');
        parenMap.put('[', ']');
        Stack<Character> stack = new Stack<>();
        for (char c: s.toCharArray())
        {
            if (parenMap.containsKey(c))
            {
                stack.push(c);
                continue;
            }
            else{
                if (c == ')' || c == '}' || c == ']')
                {
                    if (stack.isEmpty())
                    {
                        return false;
                    }
                    char top = stack.pop();
                    if (parenMap.get(top) != c)
                    {
                        return false;
                    }
                }
            }
        }
        return stack.isEmpty();
    }
}