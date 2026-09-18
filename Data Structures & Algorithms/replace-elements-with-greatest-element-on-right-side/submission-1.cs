public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int[] maxes = new int[arr.Length + 1];

        maxes[^1] = -1;
        maxes[^2] = arr[^1];

        // Skip last element
        for (int i = arr.Length - 2; i >=0 ; i--)
        {
            maxes[i] = Math.Max(arr[i], maxes[i+1]);
        }

        return maxes[1..];
        
    }
}