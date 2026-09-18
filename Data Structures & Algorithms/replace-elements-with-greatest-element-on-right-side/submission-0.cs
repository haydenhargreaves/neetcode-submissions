public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int[] maxes = new int[arr.Length];

        maxes[^1] = arr[^1];

        // Skip last element
        for (int i = arr.Length - 2; i >=0 ; i--)
        {
            maxes[i] = Math.Max(arr[i], maxes[i+1]);
        }

        Array.Resize(ref maxes, maxes.Length + 1);
        maxes[^1] = -1;

        return maxes[1..];
        
    }
}