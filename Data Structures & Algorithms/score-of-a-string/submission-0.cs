
public class Solution {
    public int ScoreOfString(string s) 
    {
        int acc = 0;

        for (var i = 0; i < s.Length - 1; i++)
        {
            acc += Math.Abs((int)s[i] - (int)s[i+1]);
        }

        return acc;
    }
}